# from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost

# Create your views here.

class BlogPageview(ListView):
    model = BlogPost
    template_name = "blog.html"

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"