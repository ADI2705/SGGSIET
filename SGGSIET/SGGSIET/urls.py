from django.contrib import admin
from django.urls import path, include
from student.views import export_student_csv, import_student_csv



urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('Faculty/', include('Faculty.urls')),
    path('department/', include('department.urls')),
    path('Account/', include('Account.urls')),
    path('Library/', include('Library.urls')),
    path('export/student/csv/', export_student_csv, name='export_student_csv'),
    path('import/student/csv/', import_student_csv, name='import_student_csv'),
    

    
]
