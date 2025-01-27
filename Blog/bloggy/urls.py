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
    path('article/add-category', views.AddCategorytView.as_view(), name='add-category'),
    path('article/category/<str:category>/', views.FilterArticleCategorytView, name='blog-category'),
    path('article/category/edit/<int:pk>/', views.UpdateCategoryView.as_view(), name='update-category'),
    path('article/category/remove/<int:pk>/', views.DeleteCategoryView.as_view(), name='delete-category'),
    path('article/category/remove/<int:pk>/', views.DeleteCategoryView.as_view(), name='delete-category'),
    path('article/category-list', views.CategoryListView, name='category-list'),
    path('article/like/<int:pk>', views.LikedPostView, name='post-like'),
    path('article/<int:pk>/comment/', views.AddCommentPostView.as_view(), name='post-comment'),
]