# Import necessary modules
from flask import Blueprint, request, jsonify
from app.models import AttendanceRecord
from bson import json_util
import json
from app.models import AttendanceRecord, User
from services.auth import token_required

# Create a new blueprint for attendance routes
attendance_route = Blueprint('attendance', __name__)

# Define a route for recording attendance
@attendance_route.route('/record', methods=['POST'])
@token_required  # Require a valid token to access this route
def record_attendance(current_user):
    # Get the JSON data from the request
    data = request.get_json()
    user_id = current_user
    # Create a new User object
    user = User(username=current_user)
    # Get the user document from the database
    user_document = user.get_user_by_username()
    print(user_document)
    # Get the enrollment ID from the user document
    enrollment_id = user_document['enrollment_id']

    # If there's no enrollment ID, return an error
    if not enrollment_id:
        return {'message': 'Enrollment ID not found'}, 400
    
    # Get the attendance data from the request
    date = data['date']
    time = data['time']
    course = data['course']
    status = data['status']
    # Create a new AttendanceRecord object
    attendance_record = AttendanceRecord(user_id, date, time, course, enrollment_id, status)
    # Save the attendance record to the database
    attendance_record.save()
    
    # Return a success message
    return {'message': 'Attendance recorded successfully'}, 200

# Define a route for getting all attendances
@attendance_route.route('/', methods=['GET'])
@token_required  # Require a valid token to access this route
def get_attendances(current_user):
    # Get all attendances from the database
    attendances = AttendanceRecord.get_all_attendances()
    # Parse the attendances into JSON format
    attendances = parse_json(attendances)
    # Return the attendances
    return jsonify({"attendances": attendances})

# Define a route for getting attendances by date
@attendance_route.route('/<date>', methods=['GET'])
@token_required  # Require a valid token to access this route
def get_attendances_by_date(current_user, date):
    # Get attendances for the specified date from the database
    attendances = AttendanceRecord.filter_attendances_by_date(date)
    # Parse the attendances into JSON format
    attendances = parse_json(attendances)
    # Return the attendances
    return jsonify({"attendances": attendances})

# Define a function for parsing data into JSON format
def parse_json(data):
    return json.loads(json_util.dumps(data))