""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import Ward
from .models_base import BaseModels


class WardModels():
    """ class containing fuctionalities for performing Person related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_ward(self, data):
        """ Add a new ward to the database """
        ward = Ward.query.filter_by(name=data['name']).first()
        if not ward:
            new_ward = Ward(
                name = data['name'],
                constituency_id = data['constituency_id']
            )
            self.models.save_changes(new_ward)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Ward with the specified name already exists..',
            }
            return response_object, 409
