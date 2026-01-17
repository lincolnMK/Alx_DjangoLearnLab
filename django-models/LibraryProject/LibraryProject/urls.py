"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from relationship_app import views as rel_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include("relationship_app.urls")),
    path('', RedirectView.as_view(url='/relationship_app/', permanent=False)), 
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', rel_views.register_view, name='register'),
]

