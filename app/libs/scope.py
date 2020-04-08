# -*- coding: UTF-8 -*-
# @Time    : 2020/2/7 10:31 下午
# @Author  : luYuZe
# @File    : scope.py
# @Project : ginger


class Scope:
    allow_api = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.A', 'v1.B']


class SuperScope(Scope):
    allow_api = ['v1.C', 'v1.D']

    def __init__(self):
        self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
