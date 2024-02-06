# student/urls.py

from django.urls import path
from .views import student_list, student_detail, export_student_csv, import_student_csv

urlpatterns = [
    path('', student_list, name='student-list'),  # Define the root URL path
    path('<int:student_id>/', student_detail, name='student-detail'),
    path('export/student/csv/', export_student_csv, name='export_student_csv'),
    path('import/student/csv/', import_student_csv, name='import_student_csv'),
]
