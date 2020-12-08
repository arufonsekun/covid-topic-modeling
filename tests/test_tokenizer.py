import unittest
import preprocessing

class TestTokenizer(unittest.TestCase):
    """ Tests tokenizer behaviour """

    def test_tokens_generation(self):
        input = "Natural Language processing is really cool."
        output = ['Natural', 'Language', 'processing', 'is', 'really', 'cool', '.']

        p = Preprocessing()
        p.set_doc(input)

        p.tokenize()

        print(p.tokens)
        assert True

if __name__ == "__main__":
    unittest.main()
