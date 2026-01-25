from urllib import request
from django.shortcuts import render
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from LibraryProject.bookshelf.models import Book

# Create your views here.

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            isbn = form.cleaned_data['isbn']
            # Save to database or perform other actions
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass    

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Logic to view a book
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {
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
