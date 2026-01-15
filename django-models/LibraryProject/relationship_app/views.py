from django.shortcuts import render

# Create your views here.

from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}  # Create a context dictionary with book list
    return render(request, 'books/book_list.html', context)

from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context da
        book = self.get_object()  # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating() 