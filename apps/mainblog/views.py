from urllib import request
from django.shortcuts import render
from  django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

# def home(request):
#     context = {}
#     return render(request, 'homepage.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']