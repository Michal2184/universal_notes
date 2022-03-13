from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('uni_notes.urls', namespace='uni_notes')),
    path('contact/', include('mailer.urls', namespace='contact'))
]
