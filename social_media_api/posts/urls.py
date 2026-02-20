from rest_framework.routers import DefaultRouter


from .views import LikePostView, PostViewSet, CommentViewSet, Feed
from django.urls import path, include


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


# Just assign the router.urls directly to urlpatterns
urlpatterns=router.urls
urlpatterns += [
    path('feed/', Feed.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', LikePostView.as_view(), name='unlike-post'),
]   