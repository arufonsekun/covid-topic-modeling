import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

DATASET_NAME = "results/preprocessing.txt"

class Topic:
    def __init__(self, n_topics):
        self.doc_file = open(DATASET_NAME, "r")
        self.doc_set = []
        self.n_topics = n_topics

    def read_document(self):
        for line in self.doc_file.readlines():
            l = line.split(",")
            l.pop(0)
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
            max_df=0.75,
            stop_words='english'
        )

        self.tfidf = tfidf_vectorizer.fit_transform(self.doc_set)
        self.features = tfidf_vectorizer.get_feature_names()

    def nmf(self):
        self._tf_idf()

        self.nmf = NMF(
            n_components=self.n_topics,
            init='nndsvd',
            max_iter=500,
            l1_ratio=0.0,
            solver='cd',
            alpha=0.0,
            tol=1e-4,
            random_state=27644434
        ).fit(self.tfidf)

        self.doc_weights = self.nmf.transform(self.tfidf)

    def generate_topics(self):
        self.n_top_words = 12
        self.topic_df = self._topic_table().T

    def print_topics(self):
        print(self.topic_df)

    def print_topic_terms_weight(self):
        weights = self.nmf.components_
        features = np.array(self.features)
        sorted_indices = np.array([list(row[::-1]) for row in np.argsort(np.abs(weights))])
        sorted_weights = np.array([list(wt[index]) for wt, index in zip(weights, sorted_indices)])
        sorted_terms = np.array([list(features[row]) for row in sorted_indices])

        topics = [np.vstack((terms.T, term_weights.T)).T for terms, term_weights in zip(sorted_terms, sorted_weights)]

        self.print_topics_udf_(topics, display_weights=True, num_terms=30)

    def _top_words(self, topic):
        return topic.argsort()[:-self.n_top_words - 1:-1] 

    def _topic_table(self):
        topics = {} 
        for topic_idx, topic in enumerate(self.nmf.components_):
            t = (topic_idx)
            topics[t] = [self.features[i] for i in self._top_words(topic)]
        return pd.DataFrame(topics)

    def print_topics_udf_(self, topics, weight_threshold=0.0001,
                     display_weights=False,
                     num_terms=None):

        for index in range(self.n_topics):
            topic = topics[index]
            topic = [(term, float(wt))
                    for term, wt in topic]
            #print(topic)
            topic = [(word, round(wt,2))
                    for word, wt in topic
                    if abs(wt) >= weight_threshold]

            if display_weights:
                print('Topic #'+str(index+1)+' with weights')
                print(topic[:num_terms]) if num_terms else topic
            else:
                print('Topic #'+str(index+1)+' without weights')
                tw = [term for term, wt in topic]
                print(tw[:num_terms]) if num_terms else tw
