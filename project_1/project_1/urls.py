# project_1/urls.py
from django.contrib import admin
from django.urls import path
from .views import hello_world_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world_view, name='hello-world'),
]