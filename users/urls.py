""" url for user login """


from django.urls import path, re_path
from django.contrib.auth.views import LoginView, logout_then_login

from . import views

app_name = 'users'

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(template_name='users/login.html'),name="login"),
    # Logout page
    path('logout/', logout_then_login ,name="logout"),
    # Registration page
    path('register/', views.register, name='register'),
]
