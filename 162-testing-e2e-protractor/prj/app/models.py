# -*- coding: utf-8; mode: python; -*-

from django.db import models


class Item(models.Model):
    content = models.CharField(max_length=100)
