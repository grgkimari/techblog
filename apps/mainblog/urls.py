from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddPostView, EditPostView,DeletePostView

urlpatterns = [
    path('',HomeView.as_view(), name = "homepage"),
    path('article/<int:pk>',ArticleView.as_view(), name = "article_view"),
    path('add_post',AddPostView.as_view(), name = "add_post"),
    path('edit_post/<int:pk>',EditPostView.as_view(), name = "edit_post"),
    path('delete_post/<int:pk>',DeletePostView.as_view(), name = "delete_post"),
]
