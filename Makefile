init:
	pip3 install -r requirements.

clean:
	py3clean .

test:
	nosetests3 tests

preprocess:
	python3 preprocessing/main.py
