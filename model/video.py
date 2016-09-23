#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Video(Base):
    id = PrimaryKeyField()
    link = CharField()
    updated_time= IntegerField(default=int(time()))

    @property
    def m_link(self):
        p_width = re.compile('width=\d+')
        p_height = re.compile('height=\d+')

        link = p_width.sub('width="100%"', self.link)
        link = p_height.sub('height="100%"', link)

        return link

    @property
    def _link(self):
        p_width = re.compile('width=\d+')
        p_height = re.compile('height=\d+')

        link = p_width.sub('width="800"', self.link)
        link = p_height.sub('height="490"', link)

        return link
