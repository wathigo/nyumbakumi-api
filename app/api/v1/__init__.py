""" import the necessary modules"""
from flask_restplus import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

""" import classes containg the endpoints """
from .views.views_user import Users

api.add_resource(Users, '/')
