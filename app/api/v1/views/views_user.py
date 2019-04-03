from flask_restful import Resource

class Users(Resource):
    """User record endpoints"""
    def __init__(self):
        pass

    def post(self):
        """ post endpoint for user registration """
        return "You a funny nigga"
