from urllib import request
from django.shortcuts import render

from LibraryProject.bookshelf.models import Book

# Create your views here.



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass    

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Logic to view a book
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {
        'books': books
    })

    

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, book_id):
    # Logic to view book details
    pass

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass 

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):  
    # Logic to delete a book
    pass    
