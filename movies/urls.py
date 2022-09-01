from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.getGenres, name='genres'),
]
