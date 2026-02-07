from .models import Book
from rest_framework import serializers
from .models import Author
from datetime import date



#book serializer to serialize the book model and validate the publication year to ensure it is not in the future
class BookSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

# author serializer to serialize the author model with a nested bookserialiser to serialize the related books dynamically, when doing the authro
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
