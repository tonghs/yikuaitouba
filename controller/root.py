#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base
from misc._route import route


@route('/')
class Investors(Base):
    def get(self):
        self.render()


@route('/danmu')
class Danmu(Base):
    def get(self):
        self.render()
