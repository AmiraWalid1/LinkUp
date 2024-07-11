#!/usr/bin/python3
""" Flask Application """
import os
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)

host = os.getenv('LinkUp_API_HOST', '0.0.0.0')
port = os.getenv('LinkUp_API_PORT', 5000)


@app.teardown_appcontext
def storageClose(exception):
    """ A method calls storage. close to teardown up """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ handle 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """ start main app """
    app.run(host=host, port=port, threaded=True)
