from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
