# student/admin.py

from django.contrib import admin
from .models import Student, Attendance

class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [AttendanceInline]

admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance)
