from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.getGenres, name='genres'),
    path('movies/', views.getMovies, name='movies'),
    path('movies/new/', views.createMovie, name='create-movie'),
    path('movies/<str:pk>/', views.getMovie, name='movie'),
    path('movies/<str:pk>/update/', views.updateMovie, name='update-movie'),
    path('movies/<str:pk>/delete/', views.deleteMovie, name='delete-movie')
]
