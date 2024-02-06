from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.Faculty_list, name='Faculty-list'),
    path('<int:Faculty_id>/', views.Faculty_detail, name='Faculty-detail'),
]
