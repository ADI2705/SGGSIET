from django.shortcuts import render
from .models import department

def department_list(request):
    departments = department.objects.all()
    print(departments)  # Add this line for debugging
    return render(request, 'department/department_list.html', {'departments': departments})


def department_detail(request, department_id):
    department = department.objects.get(id=department_id)
    # Add additional logic if needed
    return render(request, 'department/department_detail.html', {'department': department})
