""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ....utils.validators.validators_schema import CountyValidate
from ..models.models_county import CountyModels

class County(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = CountyModels()

    def post(self):
        """ test working endpoint """
        json_data = request.get_json()
        print(json_data)
        try:
            data = CountyValidate().load(json_data)
        except ValidationError as err:
            errors = err.messages
            return errors, 400
        return self.models.save_new_county(json_data)
