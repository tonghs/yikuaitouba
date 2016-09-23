#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import json

from controller._base import JsonBase, AdminBase as Base
from misc._route import route
from model.project import Project as ProjectM
from model.video import Video as VideoM
from model.user import User
from playhouse.shortcuts import model_to_dict


@route('/admin/project')
class Project(Base):
    def post(self):
        data = {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
        ProjectM(**data).save()

        self.finish()


@route('/admin/del_project')
class _(Base):
    def post(self):
        id = self.get_argument('id', 0)
        if id:
            project = ProjectM.get(ProjectM.id == id)
            if project:
                project.delete_instance()

        self.finish()

@route('/admin/edit_project')
class _(Base):
    def post(self):
        data = {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
        if data.get('id', 0):
            project = ProjectM.get(ProjectM.id == data.get('id'))
            if project:
                for k, v in data.iteritems():
                    if k == 'id':
                        pass
                    else:
                        setattr(project, k, v)

                project.save()

        self.finish()

@route('/admin/video')
class Video(Base):
    def post(self):
        link = self.get_argument('link', '')
        try:
            video = VideoM.get(VideoM.id == 1)
            video.link = link
            video.update_time = int(time())
            video.save()
        except VideoM.DoesNotExist as e:
            VideoM(link=link).save()

        self.finish()

@route('/j/admin/login')
class Login(JsonBase):
    def post(self):
        user = self.get_argument('user', '')
        pwd = self.get_argument('pwd', '')

        d = dict(user=user, pwd=pwd)

        result = False
        msg = ''
        user = User.login(**d)
        if user:
            self.set_secure_cookie("user", json.dumps(model_to_dict(user)))
            result = True
        else:
            msg = '登录失败'

        self.finish(data=dict(result=result, msg=msg))
