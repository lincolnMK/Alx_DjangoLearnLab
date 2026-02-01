from django.contrib import admin

# Register your models here.
from .models import UserProfile, Librarian, Library, Book, Author
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)


