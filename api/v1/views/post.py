#!/usr/bin/python3
"""
View for post object
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User
from models.post import Post


@app_views.route('/posts', methods=["GET"], strict_slashes=False)
def get_all_post():
    """
    Retrieves the list of all posts
    """
    posts = []
    post_obj = storage.all(Post)

    for post in post_obj.values():
        posts.append(post.to_dict())

    return (jsonify(posts))


@app_views.route('/posts/<post_id>', methods=["GET"], strict_slashes=False)
def get_post_by_id(post_id):
    """
    Retreive specific post by post id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")

    return jsonify(post.to_dict())


@app_views.route('/users/<user_id>/posts', methods=["GET"], strict_slashes=False)
def get_user_posts(user_id):
    """
    Retrieve posts of a user
    """
    posts_list = []

    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User NOt Found")

    for post in user.posts:
        posts_list.append(post.to_dict())

    return (jsonify(posts_list))


@app_views.route('/posts/<post_id>', methods=["DELETE"], strict_slashes=False)
def delete_post(post_id):
    """
    delete post by post id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")

    post.delete()
    return jsonify({}), 200


post_attrs = ['content']


@app_views.route('/users/<user_id>/posts', methods=["POST"], strict_slashes=False)
def create_post(user_id):
    """
    create new post
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Found")

    json_data = request.get_json(silent=True)
    if json_data is None:
        abort(400, 'Not a JSON')

    for attr in post_attrs:
        if attr not in json_data:
            abort(400, f'Missing <{attr}> Attribute')

    json_data['user_id'] = user_id
    post = Post(**json_data)
    post.save()
    return jsonify(post.to_dict()), 201


@app_views.route('/posts/<post_id>', methods=["PUT"], strict_slashes=False)
def update_post(post_id):
    """
    update post by post id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")

    json_data = request.get_json(silent=True)
    if json_data is None:
        abort(400, 'Not a JSON')

    ignore = ['id', 'created_at', 'updated_at', 'user_id']
    for k, v in json_data.items():
        if k not in ignore:
            setattr(post, k, v)
    storage.save()
    return jsonify(post.to_dict()), 200
