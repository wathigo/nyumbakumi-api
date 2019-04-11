""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import Constituency
from .models_base import BaseModels


class ConstituencyModels():
    """ class containing fuctionalities for performing Constituency related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_constituency(self, data):
        """ Add a new county to the database """
        constituency = Constituency.query.filter_by(name=data['name']).first()
        if not constituency:
            new_constituency = Constituency(
                name = data['name'],
                county_id = data['county_id']
            )
            self.models.save_changes(new_constituency)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Constituency already exists',
            }
            return response_object, 409
