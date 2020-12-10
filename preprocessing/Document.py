import pandas as pd
import re

class Document(object):
    """
    Document class represents a pandas DataFrame,
    also applies some raw string transformations
    """

    def __init__(self, document_name, n_rows):
        self.document_set = pd.read_csv(
                usecols = ["text", "title", "description"],
                filepath_or_buffer = document_name,
                encoding = "utf-8",
                nrows = n_rows,
                header = 0)

        self.title        = ""
        self.text         = ""
        self.description  = ""

        self.html_matcher  = re.compile("<.*?>|{href}")
        self._han_matcher  = re.compile("[A-z]*[^\u0020-\u024F]")

    """
    Removes html tags and chinese characters
    """
    def _clean_text(self):
        self.title = re.sub(self.html_matcher,"", self.title)
        self.text  = re.sub(self.html_matcher,"", self.text)
        self.description = re.sub(self.html_matcher,"", self.description)

        self.title = re.sub(self._han_matcher,"", self.title)
        self.text  = re.sub(self._han_matcher,"", self.text)
        self.description = re.sub(self._han_matcher,"", self.description)

    """
    Returns text, title and description as a single
    document transformed to lower case, given an
    document set index.
    """
    def get(self, index):
        document     = self.document_set.loc[index]
        self.title        = document["title"].lower()
        self.text         = document["text"].lower()
        self.description  = document["description"].lower()

        self._clean_text()

        return self.title +" "+ self.description +" "+ self.text
