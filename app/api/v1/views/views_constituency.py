""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ....utils.validators.validators_schema import ConstituencyValidate
from ..models.models_constituency import ConstituencyModels

class Constituency(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = ConstituencyModels()

    def post(self):
        """ Endpoint to register a new constituency record """
        json_data = request.get_json()
        print(json_data)
        try:
            data = ConstituencyValidate().load(json_data)
        except ValidationError as err:
            errors = err.messages
            return errors, 400
        return self.models.save_new_constituency(json_data)
