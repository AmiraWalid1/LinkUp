#!/usr/bin/python3
"""
View for user object
"""

from api.v1.views import app_views, storage
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/users/<user_id>', methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves the list of all User objects.

    Returns:
        - JSON: List of dictionaries representing all User objects.
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
    if not request.json:
            abort(400, 'Not a JSON')
    ignore = ['id', 'created_at', 'updated_at']
    data = request.json
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Fount")
    for k, v in data.items():
        if k not in ignore:
           setattr(user, k, v)
           user.save()
    return jsonify(user.to_dict()), 200


user_attrs = ['name', 'email', 'password']
@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user(user_id):
    """
    create user attributes
    """
    if not request.json:
        abort(400, 'Not a JSON')
    for attr in user_attrs:
        if attr not in request.json:
            abort(400, f'Missing <{attr}> Attribute')
    user = User(**request.json)
    user.save()
    return jsonify(user.to_dict()), 201
