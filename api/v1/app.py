#!/usr/bin/python3
""" Flask Application """
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


