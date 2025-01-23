from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     context = {
#         'page_name': 'Home Page',
#     }
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id'] # This makes it such that the articles are ordered such that the one higher id numbers are on top. It is advised to use dates its better.
    
class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdateArticleView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home') # This is added to redirect to the chosen page with the DeleteView avoid the following error: "No URL to redirect to. Provide a success_url."