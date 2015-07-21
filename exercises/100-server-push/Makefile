# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ     = prj
FIXTURE = eventlog/sample_data.json

all:

run-from-scratch: clean setup run

setup:
	@cd $(PRJ); \
	./manage.py makemigrations; \
	./manage.py migrate; \
	./manage.py loaddata $(FIXTURE)

run:
	@cd $(PRJ); \
	export PYTHONPATH=$$(pwd); \
	gunicorn --reload -k prj.wsgi.Worker prj.wsgi

clean:
	$(RM) $(PRJ)/db.sqlite3
	find -name "migrations" | xargs rm -rf
	find -name "*.pyc" -delete

remove-fixtures:
	$(RM) -v $(PRJ)/$(FIXTURE)

populate-db: remove-fixtures clean setup
	@cd $(PRJ); \
	export DJANGO_SETTINGS_MODULE=prj.settings; \
	./populate-db.py; \
	./manage.py dumpdata --format json --indent 4 eventlog > $(FIXTURE)

test:
	@cd $(PRJ); \
	./manage.py test
