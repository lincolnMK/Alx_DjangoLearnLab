from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView 

# Create your views here.

from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}  # Create a context dictionary with book list
    return render(request, 'books/list_books.html', context)

from django.views.generic import DetailView , ListView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context da
        book = self.get_object()  # Retrieve the current book instance
        context['book_list'] = book.objects.all()
        return context

class SignUpView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy("login")
	template_name = "relationship_app/register.html"

class BookListView(ListView):
	model = Book
	template_name =  'books/book_list.html'

