from rest_framework.routers import DefaultRouter

from accounts.views import Feed
from .views import PostViewSet, CommentViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


# Just assign the router.urls directly to urlpatterns
urlpatterns=router.urls
urlpatterns += [
    path('feed/', Feed.as_view(), name='feed'),
]   