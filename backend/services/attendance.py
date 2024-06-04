# services/attendance.py

from flask import Blueprint, request, jsonify
from app.models import AttendanceRecord
from bson import json_util

import json

from app.models import AttendanceRecord, User
from services.auth import token_required


attendance_route = Blueprint('attendance', __name__)

@attendance_route.route('/record', methods=['POST'])
@token_required
def record_attendance(current_user):
    
    data = request.get_json()
    user_id = current_user
    user = User(username=current_user)
    user_document = user.get_user_by_username()
    print(user_document)
    enrollment_id = user_document['enrollment_id']

    if not enrollment_id:
        return {'message': 'Enrollment ID not found'}, 400
    
    date = data['date']
    time = data['time']
    course = data['course']
    status = data['status']
    attendance_record = AttendanceRecord(user_id, date, time, course, enrollment_id, status)
    attendance_record.save()
    
    return {'message': 'Attendance recorded successfully'}, 200

@attendance_route.route('/', methods=['GET'])
@token_required
def get_attendances(current_user):
    attendances = AttendanceRecord.get_all_attendances()
    attendances = parse_json(attendances)
    return jsonify({"attendances": attendances})


@attendance_route.route('/<date>', methods=['GET'])
@token_required
def get_attendances_by_date(current_user, date):
    attendances = AttendanceRecord.filter_attendances_by_date(date)
    attendances = parse_json(attendances)
    return jsonify({"attendances": attendances})

def parse_json(data):
    return json.loads(json_util.dumps(data))