from flask_restplus import Resource

class Users(Resource):
    """User record endpoints"""
    def __init__(self):
        pass

    def post(self):
        """ test working endpoint """
        return {"msg": "You a funny nigga"}
