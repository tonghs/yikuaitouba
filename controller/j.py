#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _base import JsonBase
from misc._route import route

from lib.pingpp_sam.pay import start_pay


@route('/j/pay/charge')
class PayStep1(JsonBase):
    def post(self):
        channel = self.get_argument('channel', '')
        charge = start_pay(channel)
        self.finish(charge)
