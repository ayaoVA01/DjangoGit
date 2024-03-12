# from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlogPageview(ListView):
    model = BlogPost
    template_name = "blog.html"

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"
    
class BlogAddView(CreateView):
    model = BlogPost
    template_name = 'blog_add.html'
    fields = ["title",'author', 'content']
    # success_url = reverse_lazy("blogPage")
    
class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog_add.html'
    fields = ["title",'content']

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy("blogPage")
