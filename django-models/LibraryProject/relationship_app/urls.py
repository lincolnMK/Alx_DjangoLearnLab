from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, SignUpView, LibraryDetailView, admin_dashboard, librarian_dashboard, member_dashboard

# app_name = 'relationship_app'

urlpatterns = [
    # Home / books
    path('', list_books, name='home'),
    path('books/', list_books, name='books'),
    path('about/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Auth
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-based dashboards
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
    path('dashboard/', views.role_based_redirect, name='role_based_redirect'),
]
# relationship_app/urls.py
