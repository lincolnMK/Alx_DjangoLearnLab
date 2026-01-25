from django.shortcuts import render

# Create your views here.



@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass    
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    # Logic to view a book
    pass    
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    pass    
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):  
    # Logic to delete a book
    pass    
