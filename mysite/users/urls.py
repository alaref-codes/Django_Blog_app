from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# USERS URL FILE

app_name = 'blog_users'
urlpatterns = [
    path('', views.register , name='blog-register'),
    path('profile/', views.profile , name='blog-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='blog-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='blog-logout'),
]
