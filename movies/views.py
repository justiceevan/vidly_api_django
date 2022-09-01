from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Genre
from .serializer import GenreSerializer

# Create your views here.


def getGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
