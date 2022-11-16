from django.urls import path
from .views import *



urlpatterns = [
    path('album/', AlbumAPIView.as_view()),
    path('album/<str:pk>/', AlbumAPIView.as_view()) # to capture our ids
]