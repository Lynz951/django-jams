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

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        genre_instance = Genre.objects.get(genre=genre['genre'])
        song = Song.objects.create(**validated_data, genre=genre_instance)
        return song
        p(validated_data)
        p(genre)




