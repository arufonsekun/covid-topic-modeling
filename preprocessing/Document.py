import pandas as pd

class Document(object):
    """
    Document class represents a pandas DataFrame.
    """

    def __init__(self, document_name, n_rows):
        self.document_set = pd.read_csv(
            usecols = ["text", "title", "description"],
            filepath_or_buffer = document_name,
            encoding = "utf-8",
            nrows = n_rows,
            header = 0
        )

    """
    Returns text, title and description as a single
    document transformed to lower case, given an
    document set index.
    """
    def get(self, index):
        document     = self.document_set.loc[index]

        title        = document["title"].lower()
        text         = document["text"].lower()
        description  = document["description"].lower()

        return title +" "+ description +" "+ text
