# -*- mode: makefile-gmake; coding: utf-8 -*-

REPO_URL    = https://github.com/jasmine/jasmine/releases/download
RELEASE     = v2.3.4/jasmine-standalone-2.3.4.zip
JASMINE_DIR = jasmine

all:
	@echo "Visit file://$$(pwd)/tests.html"

test: download
	chromium "file://$$(pwd)/tests.html"

download: jasmine.zip

jasmine.zip:
	wget $(REPO_URL)/$(RELEASE) -O $@
	unzip -x -d $(JASMINE_DIR) $@

.PHONY: clean
clean:
	$(RM) -r $(JASMINE_DIR) jasmine.zip
