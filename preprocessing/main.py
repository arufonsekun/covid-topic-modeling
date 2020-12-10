from Preprocessing import Preprocessing
from Document import Document
import time
import subprocess

DOCUMENT_NAME = "dataset/news/news.csv"
N_ROWS        = 6786

# TODO: Check document 123

def shutdown():
    subprocess.run("shutdown")

def generate_lemmas_and_write():

    print("Generating lemmas for {} document(s) and writting...".format(N_ROWS))

    with open("results/preprocessing.txt", "w") as lemmas:

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

            l = preprocess.get_tokens_lemmas()

            lemmas.write(str(i) + "," + doc.join(l) + "\n")

            end = time.time()
            total_time += end - start
            print("Document {} took {:.2f} seconds".format(i, end - start))

    shutdown()

def main():
    generate_lemmas_and_write()

if __name__ == "__main__":
    main()
