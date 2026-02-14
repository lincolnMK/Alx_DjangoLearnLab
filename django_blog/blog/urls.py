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


from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    
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

    path('posts/post-list', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
