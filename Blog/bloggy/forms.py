from django import forms
from .models import Post, Category, Comment

category_options = Category.objects.all().values_list('name', 'name') # This returns an object with a list a queryset

# Turning the 'category_options' queryset into a python list to use for choices
category_options_list = []
for item in category_options:
    category_options_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'snippet','category', 'body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-4'},),
            'snippet': forms.Textarea(attrs={'class': 'form-control col-md-4', 'rows':4},),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control col-md-4', 'value':'', 'id':'author', 'type':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-4'}, choices = category_options), # The 'choices'  has be the first in line
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'},),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':4},),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet','category','body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows':4},),
            'category': forms.Select(choices = category_options, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'post', 'body')
        
        #Styling the fields of the form with bootsrap
        widgets = {
            'post': forms.TextInput(attrs={'class': 'form-control', 'value':'{{post.id}}', 'id':'post', 'type':'hidden'},),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'{{user.id}}', 'id':'author', 'type':'hidden'}),
            'body': forms.TextInput(attrs={'id':'comments', 'placeholder':'Enter comment...'}),
        }