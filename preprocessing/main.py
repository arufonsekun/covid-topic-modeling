from Preprocessing import Preprocessing
from Document import Document

DOCUMENT_NAME = "dataset/news/news.csv"
N_ROWS        = 1

def main():

    document_set = Document(DOCUMENT_NAME, N_ROWS)
    preprocess = Preprocessing()

    for i in range(N_ROWS):
        document = document_set.get(i)

        preprocess.set_doc(document)

        preprocess.tokenize()

        tokens = preprocess.get_tokens_text()

        print(tokens)

if __name__ == "__main__":
    main()
