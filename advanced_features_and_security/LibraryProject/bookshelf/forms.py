from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(label="Book Title", max_length=100)
    author = forms.CharField(label="Author", max_length=100)
    isbn = forms.CharField(label="ISBN", max_length=100)