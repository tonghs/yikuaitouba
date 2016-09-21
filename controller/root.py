#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base
from misc._route import route


@route('/')
class Index(Base):
    def get(self):
        self.redirect('http://comefunding.com', True)


@route('/tv')
class Index(Base):
    def get(self):
        self.render()

@route('/tv_')
class NewIndex(Base):
    def get(self):
        self.render()
