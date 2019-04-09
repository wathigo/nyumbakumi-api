""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ....utils.validators.validators_schema import PersonValidate
from ..models.models_person import PersonModels

class Person(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = PersonModels()

    def post(self):
        """ test working endpoint """
        json_data = request.get_json()
        print(json_data)
        try:
            data = PersonValidate().load(json_data)
        except ValidationError as err:
            errors = err.messages
            return errors, 400
        return self.models.save_new_person(json_data)
