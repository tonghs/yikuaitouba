#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.ioloop
import tornado.web

from config import PORT, DEBUG, HOST, COOKIE_SECRET
import _url  # noqa
from misc._route import route
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def write_error(self, status_code, **kwargs):
    if status_code == 404:
        self.render('template/404.html')

tornado.web.RequestHandler.write_error = write_error


def make_app():
    return tornado.web.Application(route.url_list, debug=DEBUG,
                                   cookie_secret=COOKIE_SECRET)

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)

    print 'Listening at {host}:{port}'.format(host=HOST, port=PORT)
    tornado.ioloop.IOLoop.current().start()
