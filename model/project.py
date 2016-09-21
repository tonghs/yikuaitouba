#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Project(Base):
    id = PrimaryKeyField()
    name = CharField()
    url = CharField()
    logo = CharField()
    investor = IntegerField(index=True)
    create_time = IntegerField(default=int(time()), index=True)

    class Meta:
        indexes = ((('investor', 'create_time'), True),)
