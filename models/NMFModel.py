import time
import numpy as np
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

DATASET_NAME = "results/preprocessing.txt"
RESULTS_PATH = "results/nmf"

class NMFModel:
    def __init__(self, n_topics,  s, b, n_top_words=10):
        self.doc_file = open(DATASET_NAME, "r")
        self.doc_set = []
        self.n_topics = n_topics
        self.n_top_words = n_top_words
        self.solver = s
        self.beta_loss = b

    def read_document(self):
        for line in self.doc_file.readlines():
            l = line.split(",")
            l.pop(0)
            # TODO treat this case in preprocessing
            try:
                l.remove("n95")
            except:
                pass
            l[-1] = l[-1].replace("\n", "")
            self.doc_set.append(" ".join(l))

    def get_docs_lenght(self):
        return len(self.doc_set)

    def get_doc_set(self):
        return self.doc_set

    def _tf_idf(self):
        tfidf_vectorizer = TfidfVectorizer(
            min_df=3,
            max_df=0.8,
            ngram_range=(1,2)
        )

        self.tfidf = tfidf_vectorizer.fit_transform(self.doc_set)
        self.features = tfidf_vectorizer.get_feature_names()

    def generate_topics(self):
        print("Generating topics...")
        print("This may take a while.")
        start = time.time()
        self._tf_idf()

        if self.solver == "cd" and self.beta_loss == "kullback-leibler":
            print("Combination of values ({} and {}) are not allowed".format(self.solver, self.beta_loss))
        else:
            print("NMF model created using solver = {} and beta_loss = {}".format(self.solver, self.beta_loss))
            self.nmf = NMF(
                n_components=self.n_topics,
                init= "nndsvd" if self.solver != "mu" else "nndsvda",
                max_iter=500,
                l1_ratio=0.0,
                solver=self.solver,
                beta_loss=self.beta_loss,
                alpha=0.0,
                tol=1e-4,
                random_state=27644434,
            ).fit(self.tfidf)

            self.topic_weights = self.nmf.transform(self.tfidf)
            end = time.time()
            print("Topic generation took {:.2f} minutes".format((end - start) / 60))

            self.extract_topics()
            self.plot_topics_wordcloud()
            self.plot_doc_per_topic()
            
    def extract_topics(self):
        self.topic_df = self._topic_table().T

    def print_topics(self):
        print("Showing top {} topics".format(self.n_topics))
        print(self.topic_df)

    def plot_topics_wordcloud(self):
        weights = self.nmf.components_
        features = np.array(self.features)
        sorted_indices = np.array([list(row[::-1]) for row in np.argsort(np.abs(weights))])
        sorted_weights = np.array([list(wt[index]) for wt, index in zip(weights, sorted_indices)])
        sorted_terms = np.array([list(features[row]) for row in sorted_indices])

        topics = [np.vstack((terms.T, term_weights.T)).T for terms, term_weights in zip(sorted_terms, sorted_weights)]

        weight_threshold = 0.0001

        for index in range(self.n_topics):
            topic = topics[index]
            topic = [(term, float(wt))
                    for term, wt in topic]

            topic = [(word, round(wt,2))
                    for word, wt in topic
                    if abs(wt) >= weight_threshold]

            plt.figure(figsize=(5,5))
            wordcloud = WordCloud(background_color="white")
            plt.imshow(wordcloud.fit_words(dict(topic[:self.n_top_words])))
            plt.axis("off")
            plt.title("Topic #{}".format(str(index+1)), fontsize=20, pad=35)

            plt.savefig("{}/{}_{}/topic_{}.png".format(RESULTS_PATH, self.beta_loss.replace("-", "_"), self.solver, index+1))

    def _top_words(self, topic):
        return topic.argsort()[:-self.n_top_words - 1:-1]

    def _topic_table(self):
        topics = {}
        for topic_idx, topic in enumerate(self.nmf.components_):
            t = (topic_idx)
            topics[t] = [self.features[i] for i in self._top_words(topic)]
        return pd.DataFrame(topics)

    def plot_doc_per_topic(self):
        docs_per_topic = {}
        for dt in range(self.topic_weights.shape[0]):
            topic_most_pr = self.topic_weights[dt].argmax()

            if topic_most_pr not in docs_per_topic:
                docs_per_topic[topic_most_pr] = 1
            else:
                docs_per_topic[topic_most_pr] += 1

        topics = list(docs_per_topic.keys())
        docs = list(docs_per_topic.values())

        docs_per_topics_plot = plt.figure(figsize=(10, 7))
        plt.bar(topics, docs)
        
        plt.title("beta_loss = {}, solver = {}".format(self.beta_loss, self.solver))
        plt.xlabel("Topic label")
        plt.ylabel("Document amount")

        plt.savefig("{}/{}_{}/docs_per_topic.png".format(RESULTS_PATH, self.beta_loss.replace("-", "_"), self.solver))
