from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.department_list, name='department-list'),
    path('<int:department_id>/', views.department_detail, name='department-detail'),
]
