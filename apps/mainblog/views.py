from audioop import reverse
from urllib import request
from django.shortcuts import render
from  django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.db.models.functions import Lower
from .forms import PostForm
from django.urls import reverse_lazy

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
    fields = ['title', 'body', 'category']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('homepage')

class AddCategoryView(CreateView):
    model = Category
    fields  = '__all__'
    template_name = 'add_category.html'

def categoryView(request, category):
  
    category_posts = [obj for obj in Post.objects.filter(category__icontains = category)]
    return render(request, 'category.html', {'category' : category, 'category_posts' : category_posts})
