#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from controller._base import Base
from misc._route import route
from model.project import Project as ProjectM
from model.video import Video as VideoM

@route('/admin/project')
class Project(Base):
    def post(self):
        data = {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
        ProjectM(**data).save()

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
