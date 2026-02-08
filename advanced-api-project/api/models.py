from django.db import models
from django_filters import rest_framework

# Create your models here.
class Author(models.Model): # this is the author model with details of the author
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Book(models.Model): # this is the book model containing details for the book including the author and publication year
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    orderingFilter = ['publication_year', 'title']

    

    def __str__(self):
        return self.title

