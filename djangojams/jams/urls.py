from django.urls import path
from .views import *



urlpatterns = [
    path('album/', AlbumAPIView.as_view()),
    path('album/<str:pk>/', AlbumAPIView.as_view()), # to capture our ids
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>/', SongAPIView.as_view())
]