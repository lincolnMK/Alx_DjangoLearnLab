# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import home
urlpatterns = [
    # Built-in authentication views
   path('', home, name='home'),  # Home page
   
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'
    ), name='login'),
    

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Custom registration view
    path('register/', views.register, name='register'),

    #just  profile view
    path('profile/', views.profile_view, name='profile'),

    # Profile editing view
    path('profile_edit/', views.profile, name='profile_edit'),

    path('post-list', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
