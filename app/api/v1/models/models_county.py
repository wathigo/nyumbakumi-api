""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import County
from .models_base import BaseModels


class CountyModels():
    """ class containing fuctionalities for performing County related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_county(self, data):
        """ Add a new county to the database """
        county = County.query.filter_by(name=data['name']).first()
        if not county:
            new_county = County(
                name = data['name']
            )
            self.models.save_changes(new_county)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'County already exists',
            }
            return response_object, 409
