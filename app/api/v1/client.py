# -*- coding: UTF-8 -*-
# @Time    : 2020/2/3 5:40 下午
# @Author  : luYuZe
# @File    : client.py
# @Project : ginger
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email,
    }
    promise[form.type.data]()
    return Success()


def _register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
