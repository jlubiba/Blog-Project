from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.title} | {self.author}'
    
    # This method allows for us to have a url to which the page can go to after the form submission to avoid the error below
    # "No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model."
    def get_absolute_url(self):
        return reverse('blog:article-details', args=(str(self.id))) # The arg refers to the article that was just created's Id as the page to load to. A url without arguments wouldn't need it
        # return reverse('blog: home') # The arg refers to the article that was just created's Id as the page to load to. A url without arguments wouldn't need it

