from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.

class AlbumAPIView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

# Read operations

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = AlbumSerializer(data)
        else:
            data = Album.objects.all()
            serializer = AlbumSerializer(data, many=True)

        return Response(serializer.data)

# Create operations

    def post(self, request, format=None):
        data = request.data
        serializer = AlbumSerializer(data=data)

        # Check if data is valid
        serializer.is_valid(raise_exception=True) 

        # Save data
        serializer.save() 

        # Save was successful, inform frontend
        response = Response()

        response.data = {
            'message': 'Album Created Successfully',
            'data': serializer.data,
        }

        return response

        # Put request

    def put(self, request, pk=None, format=None):
        album_to_update = Album.objects.get(pk=pk)
        data = request.data
        serializer = AlbumSerializer(instance=album_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Album Updated Successfully',
            'data': serializer.data
        }

        return response

# class GenreAPIView(APIView)


# class SongAPIView(APIView)

