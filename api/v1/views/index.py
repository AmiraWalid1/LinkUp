#!/usr/bin/python3
""" Index """

from models.comment import Comment
from models.like import Like
from models.user import User
from models.post import Post
from models import storage

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})
