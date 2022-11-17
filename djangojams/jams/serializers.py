from rest_framework import serializers
from .models import *
from pprint import pprint as p


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):

    genre = GenreSerializer()
    # artist = ArtistSerializer()
    # album = AlbumSerializer()
    # playlist = PlaylistSerializer()

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        genre_instance = Genre.objects.get(genre=genre['genre'])
        song = Song.objects.create(**validated_data, genre=genre_instance)
        # artist = validated_data.pop('artist')
        # artist_instance = Artist.objects.get(name=artist['name'])
        # artist_bio_instance = Artist.objects.get(bio=artist['bio'])
        # song = Song.objects.create(**validated_data, artist=artist_instance)

    #     album = validated_data.pop('album')
    #     album_instance = Album.objects.get(album=album['album'])
    #     song = Song.objects.create(**validated_data, album=album_instance)
        # playlist = validated_data.pop('playlist')
        # playlist_instance = Playlist.objects.get(title=playlist['title'])
        # song = Song.objects.create(**validated_data, playlist=playlist_instance, genre=genre['genre'])
        return song
    #     p(validated_data)
    #     p(genre)




