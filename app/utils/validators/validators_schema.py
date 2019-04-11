""" import third party modules """
from marshmallow import Schema, fields

""" local imports"""
from .validators import Views

class PersonValidate(Schema):
    """ Validate data for user registration """
    first_name = fields.Str(required=True, validate=Views().validate_all_values)
    last_name = fields.Str(required=True, validate=Views().validate_all_values)
    email = fields.Str(required=False, validate=Views().validate_email)
    national_id = fields.Int(required=True, validate=Views().validate_all_values)
    residence = fields.Boolean(required=True)
    land_id = fields.Int(required=False, validate=Views().validate_all_values)
    land_lord = fields.Boolean(required=True)
    area_id = fields.Int(required=True, validate=Views().validate_all_values)
    admin = fields.Boolean(required=False)
    password = fields.Str(required=False, validate=Views().validate_password)
    phone_number = fields.Int(required=True)

class CountyValidate(Schema):
    name = fields.Str(required=True, validate=Views().validate_all_values)

class ConstituencyValidate(Schema):
    name = fields.Str(required=True, validate=Views().validate_all_values)
    county_id = fields.Int(required=True, validate=Views().validate_all_values)

class WardValidate(Schema):
    name = fields.Str(required=True, validate=Views().validate_all_values)
    constituency_id = fields.Int(required=True, validate=Views().validate_all_values)
