""" import the necessary modules"""
from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

""" import classes containg the endpoints """
from .views.views_person import Person
from .views.views_county import County
from .views.views_constituency import Constituency
from .views.views_ward import Ward
from .views.views_area import Area

api.add_resource(Person, '/register/person')
api.add_resource(County, '/register/county')
api.add_resource(Constituency, '/register/constituency')
api.add_resource(Ward, '/register/ward')
api.add_resource(Area, '/register/area')
