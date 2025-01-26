from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdateForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     context = {
#         'page_name': 'Home Page',
#     }
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
    # This method that will allow for a context dict to be added onto the view
    def get_context_data(self, *args,**kwargs):
        category_list = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs) # The view inside is the view the method is used in
        context['category_list'] = category_list
        return context

def LikedPostView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('blog:article-details', args=[str(pk)]))

class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    # This method that will allow for a context dict to be added onto the view
    def get_context_data(self, *args,**kwargs):
        category_list = Category.objects.all()
        context = super(ArticleDetailsView, self).get_context_data(*args, **kwargs) # The view inside is the view the method is used in
        current_post = get_object_or_404(Post, id=self.kwargs['pk']) # Fetches the post for the current post's id
        total_likes = current_post.total_likes()
        
        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        # adding context elements
        context['category_list'] = category_list
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
class AddCategorytView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'

def FilterArticleCategorytView(request, category):
    items = Post.objects.filter(category=category)
    cats = Category.objects.filter(name=category)
    category_list = Category.objects.all()
    context = {
        'category': category,
        'posts': items,
        'cats': cats,
        'category_list': category_list,
    }
    return render(request, 'filter_article_category.html', context)

def CategoryListView(request):
    category_list = Category.objects.all()
    category_list = category_list.order_by('name')
    context = {
        'category_menu_list': category_list,
    }
    return render(request, 'categories.html', context)

class UpdateArticleView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home') # This is added to redirect to the chosen page with the DeleteView avoid the following error: "No URL to redirect to. Provide a success_url."

class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'update_category.html'

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('blog:home') # This is added to redirect to the chosen page with the DeleteView avoid the following error: "No URL to redirect to. Provide a success_url."