from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Genre, Movie
from .serializer import GenreSerializer, MovieSerializer

# Create your views here.


@api_view(['GET'])
def getGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
