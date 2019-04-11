""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ....utils.validators.validators_schema import AreaValidate
from ..models.models_area import AreaModels

class Area(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = AreaModels()

    def post(self):
        """ endpoint for registering a new area record """
        json_data = request.get_json()
        print(json_data)
        try:
            data = AreaValidate().load(json_data)
        except ValidationError as err:
            errors = err.messages
            return errors, 400
        return self.models.save_new_area(json_data)
