# -*- mode: makefile-gmake; coding: utf-8 -*-

.ONESHELL:
PRJ = prj

all:

setup:
	@cd $(PRJ)
	./manage.py makemigrations
	./manage.py migrate
	./manage.py loaddata app/sample_data.json

run:
	@cd $(PRJ)
	./manage.py runserver

clean:
	$(RM) $(PRJ)/db.sqlite3
	$(RM) -r $(PRJ)/migrations

test:
	@cd $(PRJ)
	./manage.py test
