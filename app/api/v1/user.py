import os

from flask import Blueprint, g, request
from flask.json import jsonify

from app.libs.error_code import DeleteSuccess, AuthFailed, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


# 查询指定用户，超级权限
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 查询本用户
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 删除指定用户
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass

# 删除本用户
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['POST'])
def create_user():
    return 'hello'


@api.route('/avatar', methods=['POST'])
def avatar():
    file = request.files['avatar_upload']
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    suffix = file.filename.rsplit('.', 1)[1][:-1]
    filename = '10002' + '.' + suffix
    file_path = os.path.join(base_path, 'static', 'images', 'uploads', filename)
    file.save(file_path)
    return Success()



