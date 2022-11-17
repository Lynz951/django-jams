from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet   
from .models import *
from .serializers import *
from rest_framework.response import Response

import csv

# Create your views here.

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

#===========================================================================================================
# class SongAPIView(APIView)

class SongAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

# Read operations

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)
        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)

# Create operations

    def post(self, request, format=None):
        data = request.data
        serializer = SongSerializer(data=data)

        # Check if data is valid
        serializer.is_valid(raise_exception=True) 

        # Save data
        serializer.save() 

        # Save was successful, inform frontend
        response = Response()

        response.data = {
            'message': 'Song Created Successfully',
            'data': serializer.data,
        }

        return response

        # Put request

    def put(self, request, pk=None, format=None):
        song_to_update = Song.objects.get(pk=pk)
        data = request.data
        serializer = SongSerializer(instance=song_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Song Updated Successfully',
            'data': serializer.data
        }

        return response

        # Delete request

    def delete(self, request, pk=None, format=None):
        song_to_delete = Song.objects.get(pk=pk)
        
        song_to_delete.delete()

        response = Response()

        response.data = {
            'message': 'Song deleted successfully',
        }

        return response


# def csv_database_write(request):

#     # Get all data from UserDetail Databse Table
#     data = [i.json() for i in MenuItems.objects.all()]

#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['id', 'title', 'description', 'pirce', 'category id', 'diet id'])

#     for item in data:
#         writer.writerow([item.get('id'), item.get('title'), item.get('description'), item.get('price'), item.get('category_id'), item.get('diet_id')])

#     return 







