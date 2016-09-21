#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller._base import Base
from misc._route import route
from model.project import Project as ProjectM

@route('/admin/project')
class Project(Base):
    def post(self):
        data = {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
        ProjectM(**data).save()

        self.finish()
