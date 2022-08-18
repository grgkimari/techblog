from django.urls import path
from . import views
from .views import HomeView, ArticleView

urlpatterns = [
    path('',HomeView.as_view(), name = "homepage"),
     path('article/<int:pk>',ArticleView.as_view(), name = "article_view"),
]
