from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamPlatform, Review

from django.shortcuts import get_object_or_404

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import (
    mixins, 
    generics,
    viewsets
)
from rest_framework.permissions import IsAuthenticated

#  ╔══════════════════════════════════╗
# ║        ⚙ Generic Views ⚙          ║
#  ╚══════════════════════════════════╝

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        #We are adding review to particular movie
        movie = WatchList.objects.get(pk=pk)
        # print(f"movie_name:: {movie} | serializer: {serializer}")

        review_user =  self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviews this movie!")
        
        serializer.save(watchlist=movie, review_user=review_user)
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        # print(f"get_queryset:: {self.kwargs}")
        # get_queryset:: {'pk': 1}
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


#  ╔══════════════════════════════════╗
# ║           ⚙ MIXINS ⚙              ║
#  ╚══════════════════════════════════╝

class ReviewDetail_TEMP(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList_TEMP(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#  ╔══════════════════════════════════╗
# ║        ⚙ Model ViewSet ⚙          ║
#  ╚══════════════════════════════════╝
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


#  ╔══════════════════════════════════╗
# ║          ⚙ ViewSets ⚙             ║
#  ╚══════════════════════════════════╝

class StreamPlatformVS_TEMP(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#  ╔══════════════════════════════════╗
# ║      ⚙ Class-Based Views ⚙        ║
#  ╚══════════════════════════════════╝

class StreamPlatformAV(APIView):
    #Object Level Permission:: Only login user can view this route
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StreamPlatformDetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            streams = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(streams)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        #pass old object & new object
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        #pass old object & new object
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response(status=status.HTTP_200_OK)



class WatchListListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)
        
#class based Basic view
class WatchListDetailsAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        #pass old object & new object
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        #pass old object & new object
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)



#  ╔══════════════════════════════════╗
# ║      ⚙ Function-Based Views ⚙     ║
#  ╚══════════════════════════════════╝

@api_view(['GET', 'POST'])
#Function Level Permission:: Only login user can view this route
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = WatchList.objects.all()
        #If we have multiple objects => many=True
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        movie = WatchList.objects.get(pk=pk)
        #pass old object & new object
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)



