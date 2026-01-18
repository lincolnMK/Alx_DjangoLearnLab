from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import permission_required
#for task 2
from django.contrib.auth import login, logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import is_librarian, is_admin, is_member
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



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create the new user
            login(request, user)  # log them in immediately
            return redirect('role_based_redirect')  # redirect to dashboard or home
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    # Your admin-specific logic here
    return render(request, 'relationship_app/admin_view.html')




@user_passes_test(is_librarian, login_url='login')
def librarian_dashboard(request):
    # Librarian-specific logic
    return render(request, 'relationship_app/librarian_view.html')



@user_passes_test(is_member, login_url='login')
def member_dashboard(request):
    # Member-specific logic
    return render(request, 'relationship_app/member_view.html')



@login_required
def role_based_redirect(request):
    role = request.user.userprofile.role
    if role == 'Admin':
        return redirect('admin_dashboard')
    elif role == 'Librarian':
        return redirect('librarian_dashboard')
    else:
        return redirect('member_dashboard')


@permission_required('relationship_app.add_book', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.delete_book', raise_exception=True)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')


