from django.urls import path
from .views import *



urlpatterns = [
    path('album/', AlbumAPIView.as_view()),
    path('album/<str:pk>/', AlbumAPIView.as_view()), # to capture our ids
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>/', SongAPIView.as_view()),
    path('genre/', GenreAPIView.as_view()),
    path('genre/<str:pk>/', GenreAPIView.as_view()),
    path('artist/', ArtistAPIView.as_view()),
    path('artist/<str:pk>/', ArtistAPIView.as_view()),
    path('playlist/', PlaylistAPIView.as_view()),
    path('playlist/<str:pk>/', PlaylistAPIView.as_view())
]