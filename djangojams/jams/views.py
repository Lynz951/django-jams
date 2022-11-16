from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet   
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.


# class AlbumAPIView(APIView):

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

        # Delete request

    def delete(self, request, pk=None, format=None):
        album_to_delete = Album.objects.get(pk=pk)

        album_to_delete.delete()

        response = Response()

        response.data = {
            'message': 'Album deleted successfully',
        }

        return response

#===========================================================================================================
# class GenreAPIView(APIView)

class GenreAPIView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

# Read operations

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = GenreSerializer(data)
        else:
            data = Genre.objects.all()
            serializer = GenreSerializer(data, many=True)

        return Response(serializer.data)

# Create operations

    def post(self, request, format=None):
        data = request.data
        serializer = GenreSerializer(data=data)

        # Check if data is valid
        serializer.is_valid(raise_exception=True) 

        # Save data
        serializer.save() 

        # Save was successful, inform frontend
        response = Response()

        response.data = {
            'message': 'Genre Created Successfully',
            'data': serializer.data,
        }

        return response

        # Put request

    def put(self, request, pk=None, format=None):
        genre_to_update = Genre.objects.get(pk=pk)
        data = request.data
        serializer = GenreSerializer(instance=genre_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Genre Updated Successfully',
            'data': serializer.data
        }

        return response

        # Delete request

    def delete(self, request, pk=None, format=None):
        genre_to_delete = Genre.objects.get(pk=pk)

        genre_to_delete.delete()

        response = Response()

        response.data = {
            'message': 'Genre deleted successfully',
        }

        return response

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


#===========================================================================================================
# class ArtistAPIView(APIView)

class ArtistAPIView(APIView):
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

# Read operations

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArtistSerializer(data)
        else:
            data = Artist.objects.all()
            serializer = ArtistSerializer(data, many=True)

        return Response(serializer.data)

# Create operations

    def post(self, request, format=None):
        data = request.data
        serializer = ArtistSerializer(data=data)

        # Check if data is valid
        serializer.is_valid(raise_exception=True) 

        # Save data
        serializer.save() 

        # Save was successful, inform frontend
        response = Response()

        response.data = {
            'message': 'Artist Created Successfully',
            'data': serializer.data,
        }

        return response

        # Put request

    def put(self, request, pk=None, format=None):
        artist_to_update = Artist.objects.get(pk=pk)
        data = request.data
        serializer = ArtistSerializer(instance=artist_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Artist Updated Successfully',
            'data': serializer.data
        }

        return response

        # Delete request

    def delete(self, request, pk=None, format=None):
        artist_to_delete = Artist.objects.get(pk=pk)
        
        artist_to_delete.delete()

        response = Response()

        response.data = {
            'message': 'Artist deleted successfully',
        }

        return response

#===========================================================================================================
# class PlaylistAPIView(APIView)

class PlaylistAPIView(APIView):
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

# Read operations

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PlaylistSerializer(data)
        else:
            data = Playlist.objects.all()
            serializer = PlaylistSerializer(data, many=True)

        return Response(serializer.data)

# Create operations

    def post(self, request, format=None):
        data = request.data
        serializer = PlaylistSerializer(data=data)

        # Check if data is valid
        serializer.is_valid(raise_exception=True) 

        # Save data
        serializer.save() 

        # Save was successful, inform frontend
        response = Response()

        response.data = {
            'message': 'Playlist Created Successfully',
            'data': serializer.data,
        }

        return response

        # Put request

    def put(self, request, pk=None, format=None):
        playlist_to_update = Playlist.objects.get(pk=pk)
        data = request.data
        serializer = PlaylistSerializer(instance=playlist_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Playlist Updated Successfully',
            'data': serializer.data
        }

        return response

        # Delete request

    def delete(self, request, pk=None, format=None):
        playlist_to_delete = Playlist.objects.get(pk=pk)
        
        playlist_to_delete.delete()

        response = Response()

        response.data = {
            'message': 'Playlist deleted successfully',
        }

        return response



