#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller._base import Base
from misc._route import route

@route('/admin/project')
class Project(Base):
    def post(self):
        arguments = {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
        print arguments

        self.finish()
