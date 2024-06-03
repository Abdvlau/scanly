# services/attendance.py

from flask import Blueprint, request
from app.models import AttendanceRecord

from app.models import AttendanceRecord


attendance_route = Blueprint('attendance', __name__)

@attendance_route.route('/record', methods=['POST'])
def record_attendance():
    
    data = request.get_json()
    user_id = data['user_id']
    class_date = data['class_date']
    status = data['status']
    remarks = data['remarks']
    modified_by = data['modified_by']
    
    attendance_record = AttendanceRecord(user_id, class_date, status, remarks, modified_by)
    attendance_record.save()
    
    return {'message': 'Attendance recorded successfully'}, 200