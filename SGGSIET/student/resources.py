# student/resources.py

from import_export import resources
from .models import Student
from django.apps import apps

Attendance = apps.get_model('student', 'Attendance')

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class AttendanceResource(resources.ModelResource):
    class Meta:
        model = Attendance
