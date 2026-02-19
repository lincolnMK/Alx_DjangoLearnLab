import token
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from posts.serializers import PostSerializer
# Create your views here.

#Implement views and serializers in the accounts app for user registration, login, and token retrieval.
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User as CustomUser
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from posts.models import Post
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

           # Get the token created in serializer
            token = Token.objects.get(user=user)
            
            return Response({
                "token": token.key,
                "user_id": user.id,
                "username": user.username
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
        ''
class follow_user(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if request.user == user_to_follow:
                return Response(
                    {'error': 'You cannot follow yourself.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if user_to_follow in request.user.following.all():
                return Response(
                    {'error': 'You are already following this user.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Add the user to follow to the list of users the current user is following
            request.user.following.add(user_to_follow)
            return Response({'status': 'User followed'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
class unfollow_user(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):

        
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)

            if request.user == user_to_unfollow:
                    return Response(
                        {'error': 'You cannot unfollow yourself.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            if user_to_unfollow not in request.user.following.all():
                    return Response(
                        {'error': 'You are not following this user.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'User unfollowed'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class followers_list(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followers = request.user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)
    
class following_list(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following = request.user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)

class Feed(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer  # required

    def get(self, request):
        following = request.user.following.all()
        posts = Post.objects.filter(author__in=following).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)