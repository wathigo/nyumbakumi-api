""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import Area
from .models_base import BaseModels


class AreaModels():
    """ class containing fuctionalities for performing Area related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_area(self, data):
        """ Add a new area to the database """
        area = Area.query.filter_by(name=data['name']).first()
        if not area:
            new_area = Area(
                name = data['name'],
                lattitude = data['lattitude'],
                longitude = data['longitude'],
                ward_id = data['ward_id']
            )
            self.models.save_changes(new_area)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Area with the specified name already exists..',
            }
            return response_object, 409
