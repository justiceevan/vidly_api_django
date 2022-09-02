from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.getGenres, name='genres'),
    path('movies/', views.getMovies, name='movies'),
    path('movies/<str:pk>/', views.getMovie, name='movie'),
    path('movies/<str:pk>/update/', views.updateMovie, name='movie-update'),
]
