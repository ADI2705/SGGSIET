# Library/models.py

from django.db import models
from student.models import Student

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"
