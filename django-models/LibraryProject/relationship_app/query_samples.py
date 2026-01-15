
books= Book.objects.filter(author="1984")

books= Book.objects.all()
print (books.all())

library = Library.objects.get(name=library_name)
librarian = library.libraries
print(librarian)