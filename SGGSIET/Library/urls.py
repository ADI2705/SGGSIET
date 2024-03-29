# Library/urls.py

from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('list/', book_list, name='book-list'),
    path('<int:book_id>/', book_detail, name='book-detail'),
]
