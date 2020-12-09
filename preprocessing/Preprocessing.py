import re
import spacy
from num2words import num2words
from spacy.lemmatizer import Lemmatizer

class Preprocessing(object):
    """
    Apply spacy preprocessing tools in a given document.
    @author Junior Vitor Ramisch <junior.ramisch@estudante.uffs.edu.br>
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
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
    Poor performance method that uses lots of NOTs
    """
    def _is_not_useless_old(self, token):
        not_punct    = not token.is_punct
        not_quote    = not token.is_quote
        not_stop_word= not token.is_stop
        not_rl_punct = not token.is_left_punct and not token.is_right_punct

        return not_stop_word and not_punct and not_quote and not_rl_punct

    def clean_tokens_old(self):
        cleaned_tokens = []
        for token in self.tokens:
            if self._is_not_useless_old(token):
                cleaned_tokens.append(token)
                self.tokens = cleaned_tokens

    """
    Check is the given token is not punctuation,
    a stop word, a quote and right or left punctuation.
    (improved _is_not_useless_old method)
    """
    def _is_not_useless(self, token):
        sw       = token.is_stop
        punct    = token.is_punct
        quote    = token.is_quote
        space    = token.is_space
        rl_punct = token.is_left_punct or token.is_right_punct

        return not (sw or punct or quote or rl_punct or space)

    """
    Removes stop word, punctuation and quote tokens.
    """
    def clean_tokens(self):
        cleaned_tokens = []
        for token in self.tokens:
            if self._is_not_useless(token):
                cleaned_tokens.append(token)
        self.tokens = cleaned_tokens

    """
    This was needed 'cause I don't wanted to use gensim,
    basically it removes unicode, and remaining punctuation
    in tokens text.
    """
    def _remove_remaining_noise(self, text):
        return re.sub(r'[^\w\s]','', text)

    def _is_float(self, text):
        return (text.find('.')+1) and text.replace('.', '', 1).isdigit()
    """
    Gets tokens lemmas, transform digits into words, and
    removes remainig punctuation as well.
    """
    # TODO: refaaactor
    def get_tokens_lemmas(self):
        lemmas = []
        text   = ""
        for token in self.tokens:
            lemma = token.lemma_
            if self._is_float(lemma):
                continue
            lemma = self._remove_remaining_noise(lemma)
            if lemma.isdigit():
                lemma = num2words(lemma).replace(" ", "_")
                lemma = lemma.replace("-", "_")
                lemma = lemma.replace(",", "_")
            if lemma != '':
                lemmas.append(lemma)
        return lemmas

    """
    Return a list of tokens text
    """
    def get_tokens_text(self):
        return [token.text for token in self.tokens]
