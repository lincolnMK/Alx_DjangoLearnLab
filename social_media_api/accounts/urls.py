from django.urls import path
from .views import LoginView, RegisterView, UserProfileView




from .views import UserProfileView, RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]