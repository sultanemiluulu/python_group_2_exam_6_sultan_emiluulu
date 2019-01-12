from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import UserInfo, Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
