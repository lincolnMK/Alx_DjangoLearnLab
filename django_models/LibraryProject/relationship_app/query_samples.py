from django.db import models
from relationship_app import Book, Librarian

books_by_author= Book.objects.filter(author="1984")
all_books= Book.objects.all()
librarians = Librarian.objects.all()