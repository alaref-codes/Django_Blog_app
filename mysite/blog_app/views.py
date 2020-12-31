from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    )

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    ordering = 'pub_date'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog_app/about.html', {'title':'About'})
