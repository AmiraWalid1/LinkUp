#!/usr/bin/python3
''' View for Like object. '''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User
from models.post import Post
from models.like import Like


@app_views.route('/posts/<post_id>/likes', methods=["GET"], strict_slashes=False)
def post_likes(post_id):
    '''Retreive all likes on post.'''
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")
    
    likes=[]
    for like in post.likes:
        likes.append(like.to_dict())
    return jsonify(likes)

@app_views.route('/users/<user_id>/likes', methods=["GET"], strict_slashes=False)
def user_likes(user_id):
    '''Retreive all likes of post.'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User Not Found")
    
    likes=[]
    for like in user.likes:
        likes.append(like.to_dict())
    return jsonify(likes)

@app_views.route('/posts/<post_id>/likes', methods=["POST"], strict_slashes=False)
def add_like(post_id):
    '''Add likes on post.'''
    json = request.get_json(silent=True)
    
    post = storage.get(Post, post_id)
    if post is None:
        abort(404, "Post Not Found")
    
    if json is None:
        abort(400, 'Not a JSON')

    if json.get('user_id') is None:
        abort(400, 'user_id Not Found.')

    json['post_id'] = post_id
    like = Like(**json)
    like.save()

    return jsonify(like.to_dict()), 201

@app_views.route('/likes/<like_id>', methods=["DELETE"], strict_slashes=False)
def remove_like(like_id):
    '''Remove likes on post.'''
    like = storage.get(Like, like_id)
    if like is None:
        abort(404, "Like Not Found")
    
    like.delete()
    return jsonify({}), 200
