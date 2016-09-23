#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict
from _base import Base
from misc._route import route
from model.project import Project
from model.video import Video


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
        li = Project.select().order_by(Project.created_time.asc())
        data = defaultdict(list)
        for o in li:
            data[o.investor].append(o)


        # 获取视频链接

        video = Video.get(Video.id == 1)

        self.render(data=data, li=li, video=video)
