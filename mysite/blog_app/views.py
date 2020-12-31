from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    ordering = 'pub_date'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['tistle','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog_app/about.html', {'title':'About'})
