#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import requests
import json

url = "http://localhost:8000/vehicle/api/"

# LIST
r = requests.get(url)
print(json.dumps(r.json(), indent=4, sort_keys=True))


# DETAIL
r = requests.get(url + "2/")
print(json.dumps(r.json(), indent=4, sort_keys=True))


# POST
r = requests.post(url + '6/', dict(brand="Ford",
                                   model="Focus",
                                   plate="1234 ABC",
                                   year=2005))
print(r)
