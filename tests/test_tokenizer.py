from ..preprocessing import Preprocessing
import unittest
import logging

class TestTokenizer(unittest.TestCase):
    """ Tests tokenizer behaviour """

    def test_tokens_generation(self):

        log = logging.getLogger( "TestTokenizer.test_tokens_generation" )

        input = "Natural Language processing is 21 really cool."
        output = ['natural', 'language', 'processing', 'is', 'twenty_one', 'really', 'cool', '.']

        p = Preprocessing.Preprocessing()
        p.set_doc(input)
        p.tokenize()
        tokens = p.get_tokens_text()

        log.debug(tokens)
        del p
        self.assertEqual(tokens, output)

if __name__ == "__main__":
    unittest.main()
