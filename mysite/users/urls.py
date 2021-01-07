from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



app_name = 'blog_users'
urlpatterns = [
    path('', views.register , name='blog-register'),
    path('profile/', views.profile , name='blog-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='blog-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='blog-logout'),


    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
            ),
        name='password-reset'
        ),

    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password-reset-done'
        ),

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password-reset-confirm'
        ),
 ]
