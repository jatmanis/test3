# example/urls.py
from django.urls import path

from example.views import index
from example.views import index1
from example.views import homeg


urlpatterns = [
    path('', index),
    path('home', index1),
    path('homeg', homeg),
]
