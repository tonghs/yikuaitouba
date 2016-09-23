#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import MYSQL
from peewee import Model, MySQLDatabase
from playhouse.shortcuts import model_to_dict, dict_to_model

db = MySQLDatabase(MYSQL.DB, user=MYSQL.USER, password=MYSQL.PWD, host=MYSQL.HOST)


class Base(Model):

    def to_dict(self):
        return model_to_dict(self)

    @classmethod
    def from_dict(cls, d):
        return dict_to_model(cls, d) if d else None

    class Meta:
        database = db


def init_db():
    from model.user import User
    from model.project import Project 
    from model.video import Video
    db.create_tables([User, Project, Video])
    import_data()


def drop_table():
    from model.user import User
    from model.project import Project 
    from model.video import Video
    db.drop_tables([User, Project, Video])


def import_data():

    li = [
        ('若饭', 'http://comefunding.com/project/projectdetail?id=13', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/1/ruofan.png', '0'),
        ('哈林秀王国际英语篮球训练营', 'http://comefunding.com', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/1/halin.png', '3'),
        ('ppgun', 'http://comefunding.com/project/projectdetail?id=14', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/1/ppgun.png', '0'),
        ('安果无人机', 'http://comefunding.com/project/projectdetail?id=15', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/1/anguo.png', '0'),
        ('王大酱', 'http://comefunding.com/project/projectdetail?id=18', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/2/wangdajiang.png', '0'),
        ('钓胃口', 'http://comefunding.com/project/projectdetail?id=28', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/2/diaoweikou_.png', '4'),
        ('kisslover', 'http://comefunding.com/project/projectdetail?id=12', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/2/kisslover.png', '4'),
        ('海军熊', 'http://comefunding.com/project/projectdetail?id=29', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/2/haijunxiong.png', '0'),
        ('H3Y', 'http://comefunding.com/project/projectdetail?id=20', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/3/h3y.png', '0'),
        ('WWAWO游区', 'http://comefunding.com/project/projectdetail?id=16', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/3/wwawo.png', '0'),
        ('三川二莲', 'http://comefunding.com/project/projectdetail?id=32', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/3/3chuan2lian.png', '3'),
        ('哲思眼镜', 'http://comefunding.com/project/projectdetail?id=30', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/3/zhesi.gif', '0'),
        ('赛果不倒蛋', 'http://comefunding.com/project/projectdetail?id=9', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/4/saiguo.png', '1'),
        ('沙米', 'http://comefunding.com/project/projectdetail?id=38', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/4/shami.png', '2'),
        ('人人安', 'http://comefunding.com', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/4/renrenan.png', '0'),
        ('粉墨宝贝', 'http://comefunding.com/project/projectdetail?id=39', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/4/fenmobaobei.png', '0'),
        ('大卫之选', 'http://comefunding.com/project/projectdetail?id=43', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/5/daweizhixuan.png', '0'),
        ('kiddie fun', 'http://comefunding.com/project/projectdetail?id=44', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/5/kiddlefun_.png', '2'),
        ('意念机', 'http://comefunding.com/project/projectdetail?id=45', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/5/yunrui.png', '0'),
        ('七天防臭袜', 'http://comefunding.com/project/projectdetail?id=46', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/5/yinsi.png', '0'),
        ('包师傅', 'http://comefunding.com/project/projectdetail?id=47', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/6/baoshifu.png', '0'),
        ('宜生到家', 'http://comefunding.com/project/projectdetail?id=11', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/6/yishengdaojia.png', '4'),
        ('缪诗', 'http://comefunding.com/project/projectdetail?id=48', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/6/miushi.png', '0'),
        ('智坐标', 'http://comefunding.com/project/projectdetail?id=49', 'http://o7ezmp5vl.bkt.clouddn.com/program/logo/6/zhizuobiao.png', '0'),
    ] 


    print "import project list..."
    from model.project import Project 
    for o in li:
        print o
        Project(name=o[0], url=o[1], logo=o[2], investor=o[3]).save()
    print "done"

    print "set video..."
    from model.video import Video
    Video(link="<iframe height=498 width=510 src='http://player.youku.com/embed/XMTcyNDcyNzA0NA==' frameborder=0 'allowfullscreen'></iframe>").save()
    print "done"

    print "insert user..."
    from model.user import User
    import hashlib
    User(user='admin', name="管理员", pwd=hashlib.md5('xxxx').hexdigest()).save()
    print "done"
