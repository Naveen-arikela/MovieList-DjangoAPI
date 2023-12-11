from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    #If we have multiple objects => many=True
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    print("pk", pk)
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

