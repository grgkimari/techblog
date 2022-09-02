from audioop import reverse
from urllib import request
from django.shortcuts import render, get_object_or_404
from  django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.db.models.functions import Lower
from .forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body', 'category']

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(EditPostView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    fields  = '__all__'
    template_name = 'add_category.html'

    def get_context_data(self, **kwargs: any) :
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context

def CategoryView(request, category):
  
    category_posts = [obj for obj in Post.objects.filter(category__icontains = category)]
    return render(request, 'category.html', {'category' : category, 'category_posts' : category_posts})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.likes.add(request.user)
    return redirect('')