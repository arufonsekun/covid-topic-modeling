import pandas as pd
from spacy.tokenizer import Tokenizer
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import English

class Preprocessing(object):
    """Apply spacy preprocessing tools in a given document."""

    def __init__(self):
        nlp = English()

    def __del__(self):
        print("Preprocessing utility destroyed")
        
    def set_doc(self, doc):
        self.doc = doc

    def tokenize(self):
        spacy_doc = nlp(self.doc)
        self.tokens = [token for token in spacy_doc]
