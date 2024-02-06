# Faculty/models.py

from django.db import models
from department.models import department

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    uid = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FacultyAttendance(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Faculty.name} - {self.date}"
