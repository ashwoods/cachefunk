.PHONY: test release

test:
	py.test

release:
	python setup.py bdist_wheel

clean:
	rm dist/*
