#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class User(Base):
    id = PrimaryKeyField()
    user = CharField(max_length=32, unique=True)
    name = CharField(max_length=32)
    pwd = CharField(max_length=32)
    created_time = IntegerField(default=int(time.time()))

    class Meta:
        indexes = ((('user', 'pwd'), True),)

    @classmethod
    def login(cls, user, pwd):
        u = None
        pwd = hashlib.md5(pwd).hexdigest()
        try:
            u = User.get(User.user == user, User.pwd == pwd)
        except User.DoesNotExist as e:
            pass

        return u
