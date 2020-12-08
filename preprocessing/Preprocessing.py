from spacy.tokenizer import Tokenizer
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import English

class Preprocessing(object):

    """
    Apply spacy preprocessing tools in a given document.
    @author Junior Vitor Ramisch <junior.ramisch@gmail.com>
    """
    def __init__(self):
        self.nlp = English()
        self.doc = ''

    """
    Class destructor
    """
    def __del__(self):
        print("Preprocessing utility destroyed")

    """
    Transform digits into text even spacy been able to
    handle digits very well.
    """
    def set_doc(self, doc):
        self.doc = doc

    """
    Generate tokens based on document previous
    transformation.
    """
    def tokenize(self):
        spacy_doc = self.nlp(self.doc)
        self.tokens = [token for token in spacy_doc]

    """
    Removes stop word, punctuation and quote tokens.
    """
    def clean_text(self):
        for token in self.tokens:
            if token.is_stop or token.is_punct or token.is_quote:
                self.tokens.remove(token)

    """
    Return a list of tokens text
    """
    def get_tokens_text(self):
        return [token.text for token in self.tokens]
