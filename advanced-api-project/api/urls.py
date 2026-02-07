from rest_framework import routers
from django.urls import path, include
from .views import (
    BookList,
    BookDetail,
    AuthorList,
    AuthorDetail,
    AuthorBooks,
    CreateBook,
    UpdateBook,
)
router = routers.DefaultRouter()
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', CreateBook.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', UpdateBook.as_view(), name='book-update'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('authors/<int:author_id>/books/', AuthorBooks.as_view(), name='author-books'),
]
