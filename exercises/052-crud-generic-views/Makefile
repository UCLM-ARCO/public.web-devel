# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ = prj

all:

setup:
	@cd $(PRJ); \
	./manage.py makemigrations; \
	./manage.py migrate; \
	./manage.py loaddata app/sample_data.json

run:
	@echo "Visit http://127.0.0.1:8000/vehicle/list/"
	@cd $(PRJ); \
	./manage.py runserver

clean:
	$(RM) $(PRJ)/db.sqlite3;
	$(RM) -r $(PRJ)/migrations/
	$(RM) -r $(PRJ)/app/static/generated
	find -name "*.pyc" -delete

test:
	@cd $(PRJ); \
	./manage.py test
