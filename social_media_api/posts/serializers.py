'''Create serializers for both Post and Comment in posts/serializers.py.
Ensure that serializers handle user relationships correctly and validate data as needed.
'''
from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
    