# Faculty/admin.py

from django.contrib import admin
from .models import Faculty, FacultyAttendance

class FacultyAttendanceInline(admin.TabularInline):
    model = FacultyAttendance
    extra = 1

class FacultyAdmin(admin.ModelAdmin):
    inlines = [FacultyAttendanceInline]

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(FacultyAttendance)
