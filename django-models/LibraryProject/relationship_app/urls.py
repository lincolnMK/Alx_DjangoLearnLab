from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('books/', views.book_list),
    path('about/', views.BookDetailView.as_view()),

    path ('login/', LoginView.as_view(template_name='relationship_app/login.html'), name ='login' ),
    path ('logout/',LogoutView.as_view(template_name='relationship_app/logout'), name = 'logout'),
    path ('register/', SignUpView.as_view(), name="register"),
]
