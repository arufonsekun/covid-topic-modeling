## Covid news topic modeling

The aim of this project is to apply [non-negative matrix fatorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization), a topic modeling approach, in a dataset of covid-19 news to extract 15 most relevant topics and then label each of them.

### Dataset

The [dataset](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26?select=news.csv) is provided by [Kaggle](https://en.wikipedia.org/wiki/Kaggle), and It contains `6786`
news articles about the coronavirus-related infectious diseases. From the original dataset was choosed `author`, `text` and `description` as principal data to compose a document.

### Preprocessing

The process related to denoising text was applied to `6786` documents following the config described previously. His aim was documents tokenization, lemmatization, and useless unit text removal like [stop words](https://en.wikipedia.org/wiki/Stop_word), digits, spaces, punctuation, HTML tags, emojis, chinese words, etc.
