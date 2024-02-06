from django.shortcuts import render
from .models import Book, BookIssue

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    # Add additional logic if needed
    return render(request, 'Library/book_detail.html', {'book': book})
