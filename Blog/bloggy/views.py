from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def home(request):
#     context = {
#         'page_name': 'Home Page',
#     }
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'