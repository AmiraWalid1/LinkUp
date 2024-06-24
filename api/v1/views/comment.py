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


@app_views.route('post/<post_id>/comments', methods=["GET"], strict_slashes=False)
def get_all_comments(post_id):
    """
    Retreive all comments of a post
    """
    comments_list = []
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not found")

    for comment in post.comments:
        comments_list.append(comment.to_dict())

    return(jsonify(comments_list))


@app_views.route('/comments/<comment_id', methods=["GET"], strict_slashes=False)
def get_comment(comment_id):
    """
    retreive comment by comment id
    """
    comment = storage.get(Comment, comment_id)
    if comment is None:
        abort(404, "Comment Not Found")

    return jsonify(comment.to_dict())


@app_views.route('/comments/<comment_id', methods=["DELETE"], strict_slashes=False)
def delete_comment(comment_id):
    """
    delete comment by  comment id
    """
    comment = storage.get(Comment, comment_id)
    if comment is None:
        abort(404, "Comment Not Found")

    comment.delete()
    storage.save()

    return jsonify({}), 200


comment_attrs = ['content', 'user_id', 'post_id']
@app_views.route('/<post_id>/comments', methods=["GET"], strict_slashes=False)
def create_commet(post_id):
    """
    create comment in a post by post id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")

    if not request.json:
        abort(400, 'Not a JSON')
    for attr in comment_attrs:
        if attr not in request.json:
            abort(400, f'Missing <{attr}> Attribute')

    comment = comment(**request.json)
    comment.save()
    return jsonify(comment.to_dict()), 201
