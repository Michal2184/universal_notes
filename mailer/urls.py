from django.urls import path
from . import views

app_name = 'mailer'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]