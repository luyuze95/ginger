# -*- coding: UTF-8 -*-
# @Time    : 2020/2/3 5:44 下午
# @Author  : luYuZe
# @File    : enums.py
# @Project : ginger
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
