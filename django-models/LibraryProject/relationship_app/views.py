from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


#for task 2
from django.contrib.auth import login, logout
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .models import Book

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add 'books' attribute dynamically to match the template
        context['library'].books = context['library'].book.all()

        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def custom_logout_view(request):
    logout(request)  # logs out the user
    return render(request, 'relationship_app/logout.html')  

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create the new user
            login(request, user)  # log them in immediately
            return redirect('relationship_app:dashboard')  # redirect to dashboard or home
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

@login_required
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})