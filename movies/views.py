from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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


@api_view(['GET'])
def getMovie(request, pk):
    movie = Movie.objects.get(_id=pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, pk):
    data = request.data

    movie = Movie.objects.get(_id=pk)

    movie.title = data['title']
    movie.numberInStock = data['numberInStock']
    movie.dailyRentalRate = data['dailyRentalRate']
    movie.genre = Genre.objects.get(_id=data['genre'])

    movie.save()

    serializer = MovieSerializer(movie, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createMovie(request):
    data = request.data

    movie = Movie.objects.create(
        title=data['title'],
        numberInStock=data['numberInStock'],
        dailyRentalRate=data['dailyRentalRate'],
        genre=Genre.objects.get(_id=data['genre'])
    )

    serializer = MovieSerializer(movie, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteMovie(request, pk):
    movie = Movie.objects.get(_id=pk)
    movie.delete()

    return Response('Movie Deleted')
