# -*- mode: makefile; coding: utf-8 -*-

examples := $(shell find -mindepth 2 -maxdepth 2 -name Makefile | xargs dirname)
examples := $(sort $(filter-out ./doc, $(examples)))

.ONESHELL:
list:
	@for d in $(examples); do
	  echo $$d
	done

test: LOG = /tmp/course-test.log
test:
	@> $(LOG)
	for d in $(examples); do
	  $(MAKE) -C $$d test >> $(LOG) 2>&1
	  echo -n .
	done
	echo
	echo OK: $$(grep OK $(LOG) | wc -l) of $(words $(examples)) examples
	echo "Full log in $(LOG)"

.PHONY: clean
clean:
	find -name "*.pyc" -delete
	find -name "*~" -delete
	for d in $(examples); do
	  $(MAKE) -C $$d clean
	done
	$(MAKE) -C doc clean
