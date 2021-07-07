.PHONY: all lint test install dev clean distclean

PYTHON ?= python

all: ;

lint:
	flake8

test: all
	py.test

install: all
	$(PYTHON) setup.py install

dev: all
	pip install -e .

clean: distclean

distclean: ;
