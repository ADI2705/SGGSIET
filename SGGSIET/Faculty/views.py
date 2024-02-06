from django.shortcuts import render
from .models import Faculty, FacultyAttendance

def Faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'Faculty/Faculty_list.html', {'Facultie': faculties})

def Faculty_detail(request, Faculty_id):
    Faculty = Faculty.objects.get(id=Faculty_id)
    attendance = FacultyAttendance.objects.filter(Faculty=Faculty)
    return render(request, 'Faculty/Faculty_detail.html', {'Faculty': Faculty, 'attendance': attendance})
