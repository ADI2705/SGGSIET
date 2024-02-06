from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.Account_list, name='Account-list'),
    path('<int:Account_id>/', views.Account_detail, name='Account-detail'),
]
