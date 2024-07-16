#!/usr/bin/python3
"""
View for user object
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/users', methods=["GET"], strict_slashes=False)
def get_all_user():
    """
    Retrieves the list of all User objects.
    """
    all_users = []
    users = storage.all(User)
    for user in users.values():
        all_users.append(user.to_dict())
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves user object with id.
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Found")
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """
    delete user object
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Found")
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/<user_id>', methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """
    A function to update user object
    """
    json_data = request.get_json(silent=True)
    if json_data is None:
        abort(400, 'Not a JSON')

    ignore = ['id', 'created_at', 'updated_at', '__class__']
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Found")

    for key, value in json_data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200


user_attrs = ['username', 'email', 'password', 'first_name', 'last_name', 'bio',
              'country', 'city']


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ create user. """
    json_data = request.get_json(silent=True)
    if json_data is None:
        abort(400, 'Not a JSON')

    for attr in user_attrs:
        if attr not in json_data:
            abort(400, f'Missing {attr} Attribute')

    user = User(**json_data)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201
