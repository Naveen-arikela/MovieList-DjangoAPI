from django.urls import path, include
# from watchlist_app.views import movie_list, movie_details
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListListAV,
    WatchListDetailsAV,
    StreamPlatformAV, 
    StreamPlatformDetailsAV,
    ReviewList,
    ReviewDetail
)


#  ╔══════════════════════════════════╗
# ║      ⚙ Class-Based URL ⚙          ║
#  ╚══════════════════════════════════╝

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details'),
    
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-list'),

]


#  ╔══════════════════════════════════╗
# ║      ⚙ Function-Based URL ⚙       ║
#  ╚══════════════════════════════════╝

"""
urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_details, name='movie-details'),
]
"""
