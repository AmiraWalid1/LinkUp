#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for
from web_flask.forms import RegistrationForm, LoginForm
from models import *
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '125381cf7c3b4af8e4659822bff66c6f'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)


@app.route('/', strict_slashes=False)
@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """returns log in page"""
    form = LoginForm()
    if form.validate_on_submit():
        for usr in storage.all(User):
            if usr.name == form.username.data:
                user = usr
            break;
        if user and check_password_hash(user.password, form.password.data):
             login_user(user)
             return redirect(url_for("home"))
        return "Your credentials are invalid."
    return render_template('login.html', form=form)


@app.route('/signUp', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """returns sign up page"""
    form = RegestrationForm()

    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data, method="sha256")
        new_user = User(name=form.username.data, email=form.email.data, password=hashed_pw)
        storage.new(new_user)
        storage.save()
        flash("You've been registered successfully, now you can log in.")
        return redirect(url_for("login"))

    return render_template('signUp.html', form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, user_id=current_user.id)
        storage.add(post)
        storage.save()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
