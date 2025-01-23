from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailsView.as_view(), name='article-details'),
    path('article/edit/<int:pk>', views.UpdateArticleView.as_view(), name='update-post'),
    path('article/remove/<int:pk>', views.DeleteArticleView.as_view(), name='delete-post'),
    path('article/add-post/', views.AddPostView.as_view(), name='add-post'),
]