from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.email = user_data["email"]
        self.password = user_data["password"]

    @staticmethod
    def get(user_id):
        from app import users_collection
        user_data = users_collection.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(user_data)
        return None
from bson.objectid import ObjectId