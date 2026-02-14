from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comment
from django.core.exceptions import ValidationError
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']  # only bio
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tags separated by commas'
            }),
        }
    def clean_content(self):
        data = self.cleaned_data.get('content', '')

        if len(data.strip()) == 0:
            raise ValidationError("Blog content cannot be empty.")

        if len(data) > 500:
            raise ValidationError("Blog cannot exceed 500 characters.")

        return data
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if len(tags) > 5:
            raise ValidationError("You can add a maximum of 5 tags.")
        return tags
   
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 5}),
        }
    def clean_content(self):
        data = self.cleaned_data['content']
        
        if len(data.strip()) == 0:
            raise ValidationError("Comment cannot be empty.")
        
        if len(data) > 500:
            raise ValidationError("Comment cannot exceed 500 characters.")
        
        return data