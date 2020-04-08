# -*- coding: UTF-8 -*-
# @Time    : 2020/2/4 10:47 下午
# @Author  : luYuZe
# @File    : base.py
# @Project : ginger
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(slient=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
