
author = Author.objects.get(name=author_name)
books_by_authr = Book.objects.filter(author=author)

books= Book.objects.all()
print (books.all())

library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian)