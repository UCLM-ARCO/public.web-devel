# -*- mode: makefile-gmake; coding: utf-8 -*-

SHELL = /bin/bash
PRJ   = prj

all:

setup:
	@cd $(PRJ); \
	./manage.py makemigrations; \
	./manage.py migrate

run:
	@cd $(PRJ); \
	export PYTHONPATH=$$(pwd); \
	./manage.py runserver &

stop:
	-PRCS=$$(ps fax | 'grep' manage.py | 'grep' -v grep); \
	while read -r line; do \
	  kill -TERM $$(echo "$$line" | cut -d" " -f1); \
	done <<< "$$PRCS"

clean:
	$(RM) $(PRJ)/db.sqlite3
	find -name "migrations" | xargs rm -rf
	find -name "*.pyc" -delete

test: clean test-start test-run test-stop

test-start: setup run
	-webdriver-manager start &
	-sleep 3

test-run:
	-protractor test-conf.js

test-stop: stop
	-PID=$$(ps fax| 'grep' webdriver-manager |'grep' -v grep |xargs |cut -d' ' -f1); \
	kill -TERM $$PID

	-PID=$$(ps fax | 'grep' selenium | 'grep' -v grep | xargs | cut -d' ' -f1); \
	kill -TERM $$PID

install-protractor:
	sudo npm install -g protractor
	sudo webdriver-manager update
