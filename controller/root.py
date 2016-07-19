#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base
from misc._route import route


@route('/')
class Pay(Base):
    def get(self):
        self.render()


@route('/pay/step/1')
class PayStep1(Base):
    def get(self):
        self.render()


@route('/investor')
class Investor(Base):
    def get(self):
        self.render()


@route('/investors')
class Investors(Base):
    def get(self):
        self.render()
