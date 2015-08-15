# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ = prj

all:

run:
	@cd $(PRJ); \
	./manage.py runserver

clean:
	$(RM) $(PRJ)/db.sqlite3
	$(RM) -r $(PRJ)/app/migrations/

test:
	@cd $(PRJ); \
	./manage.py test
