#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for, redirect, flash, abort # type: ignore
from web.forms import RegistrationForm, LoginForm, PostForm
from models.base_model import BaseModel
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
from flask_login import LoginManager, login_required, login_user, current_user # type: ignore


app = Flask(__name__)
app.config['SECRET_KEY'] = '125381cf7c3b4af8e4659822bff66c6f'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)


@app.route('/', strict_slashes=False)
@app.route('/login.html', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """returns log in page"""
    form = LoginForm()
    if form.validate_on_submit():
        for usr in storage.all(User):
            if usr.name == form.username.data:
                user = usr
            break
        if user and check_password_hash(user.password, form.password.data):
             login_user(user)
             return redirect(render_template("home.html"))
        return "Your credentials are invalid."
    return render_template('login.html', form=form)


@app.route('/signup.html', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """returns sign up page"""
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data, method="sha256")
        new_user = User(name=form.username.data, email=form.email.data, password=hashed_pw)
        storage.new(new_user)
        storage.save()
        flash("You've been registered successfully, now you can log in.")
        return redirect(url_for("login.html"))

    return render_template('signup.html', form=form)


@app.route("/home.html", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, user_id=current_user.id)
        storage.add(post)
        storage.save()
        flash('Your post has been created!', 'success')
        return redirect(render_template('home,html'))
    return render_template('home.html', form=form)


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = storage.get(Post, post_id)
    if post is None:
        abort(404)
    if post.user_id != current_user.id:
        abort(403)
    storage.delete(post)
    storage.save()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home.html'))


@app.route("/home.html")
@login_required
def home():
    posts = storage.all(Post)
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
