#!/usr/bin/make -f
# -*- mode: makefile -*-

.DEFAULT_GOAL := all

open:
	chromium --incognito http://localhost:8000
