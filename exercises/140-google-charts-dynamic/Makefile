# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ     = prj

all:

run:
	@cd $(PRJ); \
	export PYTHONPATH=$$(pwd); \
	gunicorn --reload -k prj.wsgi.Worker prj.wsgi

clean:
	$(RM) $(PRJ)/db.sqlite3
	find -name "migrations" | xargs rm -rf
	find -name "*.pyc" -delete

test:
	@cd $(PRJ); \
	./manage.py test
