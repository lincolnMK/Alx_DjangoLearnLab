from rest_framework.generics import ListAPIView
from api.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
    
class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


    
