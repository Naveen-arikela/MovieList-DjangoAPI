from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

# Create your views here.
#NOte::In this DRF we are not using these URLS

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        "movies": list(movies.values())
    }
    print(data)
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "active": movie.active
    }
    return JsonResponse(data)