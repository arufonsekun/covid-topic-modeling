from Preprocessing import Preprocessing
from Document import Document
import time
import subprocess

DOCUMENT_NAME     = "dataset/news/news.csv"
PREPROCESSED_DOCS = "results/preprocessing.csv"
N_ROWS            = 1

# TODO: Check document 123

def shutdown():
    subprocess.run("shutdown")

def generate_lemmas_and_write():

    print("Generating lemmas for {} document(s) and writting...".format(N_ROWS))

    with open("results/preprocessing.csv", "w") as lemmas:

        document_set = Document(DOCUMENT_NAME, N_ROWS)
        preprocess = Preprocessing()
        doc=","
        total_time=0
        for i in range(N_ROWS):
            start = time.time()

            document = document_set.get(i)

            preprocess.set_doc(document)

            preprocess.tokenize()

            preprocess.clean_tokens()

            l = preprocess.get_lemmas()

            lemmas.write(str(i) + "," + doc.join(l) + "\n")

            end = time.time()
            total_time += end - start
            print("Document {} took {:.2f} seconds".format(i, end - start))

    shutdown()

def generate_bigrams():
    print("Generating bigrams for {} document(s) and writting...".format(N_ROWS))

    preprocessed = open("results/preprocessing.txt", "r")

    with open("results/bigrams.csv", "w") as bigrams:

        preprocess = Preprocessing()
        doc=" "
        total_time=0

        for i, line in enumerate(preprocessed.readlines()):
            start = time.time()

            document = line.split(',')
            document.pop(0)
            document[-1] = document[-1].replace('\n', '')
            preprocess.set_doc(doc.join(document))

            preprocess.tokenize()
            preprocess.generate_bigrams()

            b = preprocess.get_bigrams()

            bigrams.write(doc.join(b) + "\n")

            end = time.time()
            total_time += end - start
            print("Document {} took {:.2f} seconds".format(i, end - start))
    print("Total time {}".format(total_time))
    
    del preprocess
    preprocessed.close()

def main():
    # generate_lemmas_and_write()
    generate_bigrams()

if __name__ == "__main__":
    main()
