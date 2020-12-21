## Covid news topic modeling

The aim of this project is to apply [non-negative matrix fatorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization), a topic modeling method, in a dataset of covid-19 news to extract 15 most relevant topics and then label each of them.

### Dataset

The [dataset](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26?select=news.csv) is provided by [Kaggle](https://en.wikipedia.org/wiki/Kaggle), and contains `6786`
news articles about the coronavirus-related infectious diseases.
The content of `author`, `text` and `description` was selected columns to compose a document.

### Preprocessing

The process related to denoising text, wich is composed by tokenization, lemmatization, and useless unit text removal like [stop words](https://en.wikipedia.org/wiki/Stop_word), digits, spaces, punctuation, HTML tags, emojis, chinese words, etc.
