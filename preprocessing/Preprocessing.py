import re
import spacy

class Preprocessing(object):
    """
    Apply spacy preprocessing tools in a given document.
    @author Junior Vitor Ramisch <junior.ramisch@estudante.uffs.edu.br>
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")

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
        self.doc = self.nlp(doc)

    """
    Generate tokens based on document previous
    transformation.
    """
    def tokenize(self):
        self.tokens = [token for token in self.doc]

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
        sw           = token.is_stop
        punct        = token.is_punct
        quote        = token.is_quote
        rl_punct     = token.is_left_punct or token.is_right_punct
        space        = token.is_space
        is_digit     = token.is_digit
        is_len_ltn_3 = len(token.text) < 3
        is_currency  = token.is_currency

        return not (sw or punct or quote or rl_punct or space or is_digit or is_currency or is_len_ltn_3)

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
    def get_lemmas(self):
        lemmas = []
        text   = ""
        for token in self.tokens:
            lemma = self._remove_remaining_noise(token.lemma_)
            if self._is_float(lemma) or lemma.isdigit():
                continue
            if lemma != '' and len(lemma) > 2:
                lemmas.append(lemma)
        return lemmas

    """
    Return a list of tokens text
    """
    def get_tokens(self):
        return [token.text for token in self.tokens]

    def generate_bigrams(self):
        for noun_phrase in list(self.doc.noun_chunks):
            noun_phrase.merge(noun_phrase.root.tag_, noun_phrase.root.lemma_, noun_phrase.root.ent_type_)

    def get_bigrams(self):
        tokens = []
        for token in self.tokens:
            if len(token.text.split(" ")) == 2:
                tokens.append(token.text.replace(" ", "_"))
            else:
                tokens.append(token.text)
        return tokens
