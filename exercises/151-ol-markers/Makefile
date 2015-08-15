# -*- mode: makefile-gmake; coding: utf-8 -*-

PRJ       = prj
FIXTURE   = eventlog/sample_data.json
# MAP_URL   = http://www.hooverae.com/mastermiddleearth.jpg
MAP_URL   = http://thefolkes.com/pictures/theater/MiddleEarth.jpg
MAP_FILE  = middle-earth.jpg
TILES_DIR = prj/maps/static/maps/tiles

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

gen-tiles: $(MAP_FILE)
	$(RM) $(TILES_DIR) -r
	tools/tile-maker.py -z 7 --output $(TILES_DIR) $<

$(MAP_FILE):
	wget $(MAP_URL) -O $(MAP_FILE)

remove-fixtures:
	$(RM) -v $(PRJ)/$(FIXTURE)

populate-db: remove-fixtures clean setup
	@cd $(PRJ); \
	export DJANGO_SETTINGS_MODULE=prj.settings; \
	./populate-db.py; \
	./manage.py dumpdata --format json --indent 4 auth.User eventlog > $(FIXTURE)

test:
	@cd $(PRJ); \
	./manage.py test
