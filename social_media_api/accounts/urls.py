from django.urls import path
from .views import LoginView, RegisterView, UserProfileView, follow_user, unfollow_user




from .views import UserProfileView, RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user.as_view(), name='follow'),  # Update the URL
    path('unfollow/<int:user_id>/', unfollow_user.as_view(), name='unfollow'),
   
    
]

