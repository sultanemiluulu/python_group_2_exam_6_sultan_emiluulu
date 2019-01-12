from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from webapp.models import UserInfo, Post
from webapp.forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseForbidden


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if self.request.user == post.author:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            return redirect('accounts:login')
        else:
            return redirect('webapp:post_detail', pk=kwargs['pk'])


class PostDeleteView(LoginRequiredMixin, View):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('webapp:post_list')

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if self.request.user == post.author:
            return super(PostDeleteView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            return redirect('accounts:login')
        else:
            return redirect('webapp:post_detail',  pk=kwargs['pk'])




