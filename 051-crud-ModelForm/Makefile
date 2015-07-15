# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ = prj

all:

setup:
	@cd $(PRJ); \
	./manage.py makemigrations; \
	./manage.py migrate; \
	./manage.py loaddata app/sample_data.json

run:
	@cd $(PRJ); \
	./manage.py runserver; \
	echo "http://127.0.0.1:8000/add-vehicle/"

clean:
	$(RM) $(PRJ)/db.sqlite3;
	$(RM) -r $(PRJ)/migrations/


test:
	@cd $(PRJ); \
	./manage.py test
