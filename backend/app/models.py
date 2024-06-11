# Import necessary modules
from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to the MongoDB client
client = MongoClient("mongodb+srv://scanly:admin@cluster0.lxv1b75.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# Select the database
db = client['myCollection']

# Define the User class
class User:
    # Initialize a new User object
    def __init__(self, username, email=None, enrollment_id=None, password_hash=None, last_login=None, profile_picture=None):
        self.username = username
        self.email = email
        self.enrollment_id = enrollment_id
        self.password_hash = password_hash
        self.last_login = last_login
        self.profile_picture = profile_picture

    # Define a method to save the user to the database
    def save(self):
        # Select the users collection
        users_collection = db['users']
        # Create a dictionary with the user's data
        user_data = {
            'username': self.username,
            'email': self.email,
            'enrollment_id': self.enrollment_id,
            'password_hash': self.password_hash,
            'last_login': self.last_login,
            'profile_picture': self.profile_picture
        }
        # Insert the user data into the users collection
        users_collection.insert_one(user_data)
        
    # Define a method to get a user by username
    def get_user_by_username(self):
        # Select the users collection
        users_collection = db['users']
        # Find the user document with the given username
        user_document = users_collection.find_one({'username': self.username})
        # If a user document is found, return it
        if user_document:
            return user_document
        # If no user document is found, return None
        else:
            return None

    # Define a method to get a user by id
    def get_user_by_id(self, user_id):
        # Select the users collection
        users_collection = db['users']
        # Find the user document with the given id
        user_document = users_collection.find_one({'_id': ObjectId(user_id)})
        # If a user document is found, return a User object with the document's data
        if user_document:
            return User(**user_document)
        # If no user document is found, return None
        else:
            return None

# Define the AttendanceRecord class
class AttendanceRecord:
    # Initialize a new AttendanceRecord object
    def __init__(self, user_id, date, time, course, enrollment_id, status=None):
        self.user_id = user_id
        self.date = date
        self.time = time
        self.course = course
        self.status = status
        self.enrollment_id = enrollment_id

        # Select the attendance_records collection
        self.attendance_collection = db['attendance_records']

    # Define a method to save the attendance record to the database
    def save(self):
        # Select the attendance_records collection
        attendance_collection = self.attendance_collection
        # Create a dictionary with the attendance record's data
        attendance_data = {
            'user_id': self.user_id,
            'date': self.date,
            'time': self.time,
            'status': self.status,
            "course": self.course,
            "enrollment_id": self.enrollment_id
        }
        # Insert the attendance data into the attendance_records collection
        attendance_collection.insert_one(attendance_data)

    # Define a class method to get all attendance records
    @classmethod
    def get_all_attendances(cls):
        # Select the attendance_records collection
        attendance_collection = db['attendance_records']
        # Return all documents in the collection
        return list(attendance_collection.find())

    # Define a class method to filter attendance records by date
    @classmethod
    def filter_attendances_by_date(cls, date):
        # Select the attendance_records collection
        attendance_collection = db['attendance_records']
        # Return all documents in the collection that have the given date
        return list(attendance_collection.find({'date': date}))