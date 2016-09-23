#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from model._base import drop_table, init_db


def main():
    # drop_table()
    init_db()

def test_user_login(user, pwd):
    from model.user import User
    return User.login(user, pwd)


if __name__ == '__main__':
    print test_user_login('admin', 'OhMyGod20!@')
