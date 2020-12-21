## Covid news topic modeling

The aim of this project is to apply [non-negative matrix fatorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization), a topic modeling approach, in a dataset of covid-19 news to extract 15 most relevant topics and then label each of them.

### Dataset

The [dataset](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26?select=news.csv) is provided by [Kaggle](https://en.wikipedia.org/wiki/Kaggle), and It contains `6786`
news articles about the coronavirus-related infectious diseases. From the original dataset was choosed `author`, `text` and `description` as principal data to compose a document.

### Preprocessing

The process related to denoising text was applied to `6786` documents following the config described previously. His aim was documents tokenization, lemmatization, and useless unit text removal like [stop words](https://en.wikipedia.org/wiki/Stop_word), digits, spaces, punctuation, HTML tags, emojis, chinese words, etc.

### Feature Extraction

The method used for feature extraction was [TF─IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), wich is described by wikipedia as a numerical estatistic that describes how much a **term/word** is relevant to a **document** in the perspective of a collection of **documents** (aka corpus). In other words if a term appears very often accros documents his TFIDF score will be low wich means the term ins't meaninfull, in the contrary if the frequency of the term is considerably low across documents and very high in a few of them, then TFIDF score will be high, so We can conclude the term is interesting and carries a lot of meaning.

### Topic Modeling

Non-negative matrix fatorization is a set o algorithms that aims to factorize a matrix **V** into two distict matrices **W** and **H** that match in dimentions (that simple rule taught in linear algebra courses) ...
