from django.urls import path
from . import views

app_name = 'blog-users'
urlpatterns = [
    path('register/', views.register , name='blog-register'),
]
