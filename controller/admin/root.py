#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller._base import Base, AdminBase
from misc._route import route

from model.project import Project as Project_
from playhouse.shortcuts import model_to_dict


@route('/admin')
@route('/admin/')
@route('/admin/index')
class Index(AdminBase):
    def get(self):
        self.render()


@route('/admin/edit')
class Edit(AdminBase):
    def get(self):
        id = self.get_argument('id', 0)

        project = None
        if id:
            try:
                project = Project_.get(Project_.id == id)
            except Project_.DoesNotExist as e:
                pass

        self.render(project=model_to_dict(project))


@route('/admin/video-mgr')
class Video(AdminBase):
    def get(self):
        self.render()


@route('/admin/project-list')
class Project(AdminBase):
    def get(self):
        li = Project_.select().order_by(Project_.created_time.desc())

        self.render(li=li)


@route('/admin/login')
class Login(Base):
    def get(self):
        self.render()


@route('/admin/logout')
class Logout(Base):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/admin/login')
