init:
	pip3 install -r requirements.

clean:
	py3clean .

test_lemmatizer:
	nosetests3 tests/test_preprocessing.py:TestLemmatizer.compare_document_lemmas

test_tokenizer:
	nosetests3 tests/test_preprocessing.py:TestTokenizer

test_reading_issue:
	nosetests3 tests/test_preprocessing.py:TestLemmatizer.test_problematic_document

preprocess:
	python3 preprocessing/main.py
