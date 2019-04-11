""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ....utils.validators.validators_schema import WardValidate
from ..models.models_ward import WardModels

class Ward(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = WardModels()

    def post(self):
        """ endpoint for registering a new ward record """
        json_data = request.get_json()
        print(json_data)
        try:
            data = WardValidate().load(json_data)
        except ValidationError as err:
            errors = err.messages
            return errors, 400
        return self.models.save_new_ward(json_data)
