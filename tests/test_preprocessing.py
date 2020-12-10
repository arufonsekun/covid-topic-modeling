from ..preprocessing import Preprocessing
from ..preprocessing import Document
import unittest
import logging

DOCUMENT_NAME = "dataset/news/news.csv"
N_ROWS        = 3

class TestTokenizer(unittest.TestCase):
    """
    Tests tokenizer behaviour
    """
    def test_tokens_generation(self):
        preprocess = Preprocessing.Preprocessing()
        log = logging.getLogger( "TestTokenizer.test_tokens_generation" )

        input = "Natural Language processing is 21 really cool."
        output = ['Natural', 'Language', 'processing', '21', 'cool']

        preprocess.set_doc(input)
        preprocess.tokenize()
        preprocess.clean_tokens()
        tokens = preprocess.get_tokens_text()

        log.debug(tokens)
        self.assertEqual(tokens, output)

    """
    Test clean_tokens() and clean_tokens_old(),
    if an error raises it's OK, It supposed to,
    diff output1.txt output2.txt for more details.
    """
    def test_tokens_cleaning(self):

        preprocess = Preprocessing.Preprocessing()
        doc_set = Document.Document(DOCUMENT_NAME, N_ROWS)

        doc = doc_set.get(0)

        log = logging.getLogger("TestTokenizer.test_tokens_cleaning")

        with open("output1.txt", "w") as output1:
            preprocess.set_doc(doc)
            preprocess.tokenize()
            preprocess.clean_tokens()
            lemmas1 = preprocess.get_tokens_lemmas()

            for lemma in lemmas1:
                output1.write(lemma+'\n')

        with open("output2.txt", "w") as output2:
            preprocess.set_doc(doc)
            preprocess.tokenize()
            preprocess.clean_tokens_old()
            lemmas2 = preprocess.get_tokens_lemmas()

            for lemma in lemmas2:
                output2.write(lemma+'\n')

        del preprocess
        del doc_set

        self.assertEquals(lemmas1, lemmas2)

class TestLemmatizer(unittest.TestCase):

    def compare_document_lemmas(self):
        preprocess = Preprocessing.Preprocessing()
        doc_set = Document.Document(DOCUMENT_NAME, N_ROWS)

        doc = doc_set.get(2)

        preprocess.set_doc(doc)
        preprocess.tokenize()
        preprocess.clean_tokens()

        with open("output3.txt", "w") as output1:
            texts = preprocess.get_tokens_text()

            for text in texts:
                output1.write(text+'\n')

        with open("output4.txt", "w") as output2:
            lemmas = preprocess.get_tokens_lemmas()

            for lemma in lemmas:
                output2.write(lemma+'\n')

        del preprocess
        del doc_set

    """
    Document 3499 has 2 commas in sequence
    fucking up my reading process.
    """
    def test_problematic_document(self):

        log = logging.getLogger("TestLemmatizer.test_problematic_document")

        n_rows = 3501
        preprocess = Preprocessing.Preprocessing()

        try:
            doc_set = Document.Document(DOCUMENT_NAME, n_rows)
            doc = doc_set.get(3500)
            assert True
        except:
            assert False

        del preprocess
        del doc_set

    def log_test_cleaning(self):
        log = logging.getLogger("TestLemmatizer.test_url_html_cleaning")

        n_rows = 134
        doc_set = Document.Document(DOCUMENT_NAME, n_rows)
        preprocess = Preprocessing.Preprocessing()

        doc = doc_set.get(131)

        preprocess.set_doc(doc)
        preprocess.tokenize()

        preprocess.clean_tokens()

        log.debug(preprocess.get_tokens_text())

        log.debug(preprocess.get_tokens_lemmas())

        assert False

if __name__ == "__main__":
    unittest.main()
