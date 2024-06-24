#!/usr/bin/python3
"""
View for post object
"""

from api.v1.views import app_views, storage
from flask import jsonify, abort, request
from models import storage
from models.user import User
from models.post import Post
from models.comment import Comment


@app_views.route('/posts/<post_id>/comments', methods=["GET"], strict_slashes=False)
def post_comments(post_id):
    """
    Retreive all comments of a post
    """
    comments_list = []
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not found")

    for comment in post.comments:
        comments_list.append(comment.to_dict())

    return (jsonify(comments_list))


@app_views.route('/users/<user_id>/comments', methods=["GET"], strict_slashes=False)
def user_comments(user_id):
    """
    Retreive all comments of a user
    """
    comments_list = []
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not found")

    for comment in user.comments:
        comments_list.append(comment.to_dict())

    return (jsonify(comments_list))


@app_views.route('/comments/<comment_id>', methods=["GET"], strict_slashes=False)
def get_comment(comment_id):
    """
    retreive comment by comment id
    """
    comment = storage.get(Comment, comment_id)
    if comment is None:
        abort(404, "Comment Not Found")

    return jsonify(comment.to_dict())


@app_views.route('/comments/<comment_id>', methods=["DELETE"], strict_slashes=False)
def delete_comment(comment_id):
    """
    delete comment by  comment id
    """
    comment = storage.get(Comment, comment_id)
    if comment is None:
        abort(404, "Comment Not Found")

    comment.delete()
    return jsonify({}), 200


comment_attrs = ['content', 'user_id']


@app_views.route('/posts/<post_id>/comments', methods=["POST"], strict_slashes=False)
def create_comment(post_id):
    """
    Create comment in a post by post id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")

    json = request.get_json(silent=True)
    if not json:
        abort(400, 'Not a JSON')

    for attr in comment_attrs:
        if attr not in json:
            abort(400, f'Missing <{attr}> Attribute')

    json['post_id'] = post_id
    comment = Comment(**json)
    comment.save()
    return jsonify(comment.to_dict()), 201


@app_views.route('/comments/<comment_id>', methods=['PUT'], strict_slashes=False)
def update_comment(comment_id):
    ''' Update a Comment by comment_id. '''
    json = request.get_json(silent=True)
    if not json:
        abort(400, 'Not a JSON')

    comment = storage.get(Comment, comment_id)
    if not comment:
        abort(404, "Comment Not Found")

    ignore = ['id', 'created_at', 'updated_at', 'user_id', 'post_id']
    for key, value in json.items():
        if key not in ignore:
            setattr(comment, key, value)
    storage.save()
    return jsonify(comment.to_dict()), 200
