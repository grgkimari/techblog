from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddPostView

urlpatterns = [
    path('',HomeView.as_view(), name = "homepage"),
    path('article/<int:pk>',ArticleView.as_view(), name = "article_view"),
    path('add_post',AddPostView.as_view(), name = "add_post"),
]
