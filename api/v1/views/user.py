#!/usr/bin/python3
"""
View for user object
"""

from api.v1.views import app_views, storage
from flask import jsonify, abort, request
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


