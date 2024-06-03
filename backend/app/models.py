# model.py
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
db = client['myCollection']

class User:
    def __init__(self, username, email=None, role=None, password_hash=None, last_login=None, profile_picture=None):
        self.username = username
        self.email = email
        self.role = role
        self.password_hash = password_hash
        self.last_login = last_login
        self.profile_picture = profile_picture

    def save(self):
        users_collection = db['users']
        user_data = {
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'password_hash': self.password_hash,
            'last_login': self.last_login,
            'profile_picture': self.profile_picture
        }
        users_collection.insert_one(user_data)
        
    def get_user_by_username(self):
        users_collection = db['users']
        user_document = users_collection.find_one({'username': self.username})
        if user_document:
            return user_document
        else:
            return None

    def get_user_by_id(self, user_id):
        users_collection = db['users']
        user_document = users_collection.find_one({'_id': ObjectId(user_id)})
        if user_document:
            return User(**user_document)
        else:
            return None

class AttendanceRecord:
    def __init__(self, user_id, class_date, status=None, remarks=None, modified_by=None):
        self.user_id = user_id
        self.class_date = class_date
        self.status = status
        self.remarks = remarks
        self.modified_by = modified_by

    def save(self):
        attendance_collection = db['attendance_records']
        attendance_data = {
            'user_id': self.user_id,
            'class_date': self.class_date,
            'status': self.status,
            'remarks': self.remarks,
            'modified_by': self.modified_by
        }
        attendance_collection.insert_one(attendance_data)

# Define other models similarly
