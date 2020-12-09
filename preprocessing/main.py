from Preprocessing import Preprocessing
from Document import Document

DOCUMENT_NAME = "dataset/news/news.csv"
N_ROWS        = 3

def main():

    document_set = Document(DOCUMENT_NAME, N_ROWS)
    preprocess = Preprocessing()

    # for i in range(N_ROWS):
    document = document_set.get(2)

    preprocess.set_doc(document)

    preprocess.tokenize()

    preprocess.clean_tokens()

    lemmas = preprocess.get_tokens_lemmas()

    print(len(lemmas))
    print(lemmas)

if __name__ == "__main__":
    main()
