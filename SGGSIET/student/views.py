from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tablib import Dataset
from .resources import StudentResource 
from .models import Student
from django.shortcuts import render



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    attendance = Attendance.objects.filter(student=student)
    return render(request, 'student/student_detail.html', {'student': student, 'attendance': attendance})
    
def export_student_csv(request):
    student_resource = StudentResource()
    dataset = student_resource.export()

    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    return response

def import_student_csv(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        imported_data = dataset.load(new_student.read().decode('utf-8'), format='csv')
        result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(dataset, dry_run=False)  # Import the actual data


    return render(request, 'import.html')
