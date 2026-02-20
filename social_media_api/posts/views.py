
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Like, Post, Comment
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics, permissions, status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Create your views here.
# List all posts
'''View Implementation:
Using Django REST Framework’s viewsets, set up CRUD operations for both posts and comments in posts/views.py.
Implement permissions to ensure users can only edit or delete their own posts and comments.'''

#permissions
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Anyone can read
    - Only owner can update/delete
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if object has author attribute
        return obj.author == request.user


#viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Feed(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer  # required

    def get(self, request):
       
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
       

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
  


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
 #Like.objects.get_or_create(user=request.user, post=post)"]
        content_type = ContentType.objects.get_for_model(post)

        # If already liked → UNLIKE
        if not created:
            like.delete()

            # Delete existing notification
            Notification.objects.filter(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                content_type=content_type,
                object_id=post.id
            ).delete()

            return Response(
                {"status": "unliked"},
                status=status.HTTP_200_OK
            )

        # If newly liked → create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                content_type=content_type,
                object_id=post.pk
            )

        return Response(
            {"status": "liked"},
            status=status.HTTP_201_CREATED
        )
    #Like.objects.get_or_create(user=request.user, post=post)"]