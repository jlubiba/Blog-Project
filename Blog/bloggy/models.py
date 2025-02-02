from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('blog:home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='post_likes')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.title} | {self.author}'
    
    # This method allows for us to have a url to which the page can go to after the form submission to avoid the error below
    # "No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model."
    def get_absolute_url(self):
        return reverse('blog:article-details', args=[str(self.id)]) # The arg refers to the article that was just created's Id as the page to load to. A url without arguments wouldn't need it
        # return reverse('blog: home') # The arg refers to the article that was just created's Id as the page to load to. A url without arguments wouldn't need it
        
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Comment...')
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post.title} by {self.author.username}'
    
    def get_absolute_url(self):
        return reverse('blog:article-details', args=[str(self.post.pk)]) 

