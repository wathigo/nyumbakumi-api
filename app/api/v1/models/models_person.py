""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import Person
from .models_base import BaseModels


class PersonModels():
    """ class containing fuctionalities for performing Person related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_person(self, data):
        """ Add a new user to the database """
        person = Person.query.filter_by(email=data['email']).first()
        if not person:
            new_person = Person(
                first_name=data['first_name'],
                last_name = data['last_name'],
                national_id = data['national_id'],
                phone_number = data['phone_number'],
                residence = data['residence'],
                land_id = data['land_id'],
                land_lord = data['land_lord'],
                area_id = data['area_id'],
                admin = data['admin'],
                password = data['password'],
                email=data['email'],
                registered_on=datetime.datetime.utcnow()
            )
            self.models.save_changes(new_user)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
