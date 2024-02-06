# Account/models.py

from django.db import models
from department.models import department
from student.models import Student
from Faculty.models import Faculty

class Account(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    
    # For students
    fees_paid = models.BooleanField(default=False)
    
    # For Faculty
    salary_paid = models.BooleanField(default=False)
    
    # Add other fields related to Account
    
    def __str__(self):
        return f"Account: {self.student.name if self.student else ''} - {self.Faculty.name if self.Faculty else ''} - {self.department.name if self.department else ''}"
