#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller._base import Base
from misc._route import route


@route('/admin')
@route('/admin/')
@route('/admin/index')
class Index(Base):
    def get(self):
        self.render()
