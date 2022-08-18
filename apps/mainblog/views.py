from urllib import request
from django.shortcuts import render
from  django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     context = {}
#     return render(request, 'homepage.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'
