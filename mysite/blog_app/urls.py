from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='blog-detail'),
    path('post/new/', PostCreateView.as_view() , name='blog-create'),
    path('about/', views.about , name='blog-about'),
]
