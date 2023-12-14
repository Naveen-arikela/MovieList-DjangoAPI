from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from watchlist_app.views import movie_list, movie_details
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListListAV,
    WatchListDetailsAV,
    StreamPlatformAV, 
    StreamPlatformDetailsAV,
    StreamPlatformVS,
    ReviewList,
    ReviewDetail,
    ReviewCreate
)

router = DefaultRouter()
#This router will handle:: stream and stream/1
router.register('stream', StreamPlatformVS, basename='streamplatfrom')


#  ╔══════════════════════════════════╗
# ║      ⚙ Class-Based URL ⚙          ║
#  ╚══════════════════════════════════╝

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='movie-details'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-details'),
    path('', include(router.urls)),

    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-list'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
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
