# -*- coding: UTF-8 -*-
# @Time    : 2020/2/5 7:55 下午
# @Author  : luYuZe
# @File    : token.py
# @Project : ginger
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
        "token": token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
