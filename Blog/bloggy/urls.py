from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailsView.as_view(), name='article-details'),
]