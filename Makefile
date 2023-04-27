SHELL=/bin/bash

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

install:
	python3 -m pip install --upgrade build

build:
	python3 -m build 

deploy:
	twine upload dist/*