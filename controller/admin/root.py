#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller._base import Base, AdminBase
from misc._route import route


@route('/admin')
@route('/admin/')
@route('/admin/index')
class Index(AdminBase):
    def get(self):
        self.render()


@route('/admin/video-mgr')
class Video(AdminBase):
    def get(self):
        self.render()


@route('/admin/login')
class Login(Base):
    def get(self):
        self.render()


@route('/admin/logout')
class Logout(Base):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/admin/login')
