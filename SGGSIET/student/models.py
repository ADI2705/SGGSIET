# student/models.py

from django.db import models
from department.models import department

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
