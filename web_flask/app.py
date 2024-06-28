#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '125381cf7c3b4af8e4659822bff66c6f'


@app.route('/', strict_slashes=False)
@app.route('/login', strict_slashes=False)
def login():
    """returns log in page"""
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signUp', strict_slashes=False)
def signup():
    """returns sign up page"""
    form = RegestrationForm()
    return render_template('signUp.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
