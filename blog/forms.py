from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'name-from-django'}),
            'body': forms.Textarea(attrs={'class': 'name-from-django'}),
        }