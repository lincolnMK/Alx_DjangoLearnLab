
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import views
from api.views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]