# from django.shortcuts import render
from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):

    # model = Post
    paginate_by = 5  
    context_object_name = 'posts'
    
    def get_queryset(self):
        contex = Post.objects.filter(status=True).order_by('-id')
        return contex

    def get_template_names(self):
        template_name = 'blog/post_list.html'
        return template_name
    



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Replace with your template name
    context_object_name = 'post'


    