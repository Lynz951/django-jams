from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField()

# class Genre(models.Model):
#     genre = models.CharField(max_length=100)

# class Song(models.Model):
#     title = models.CharField(max_length=200)
#     duration = models.FloatField()
#     num_of_plays = models.IntegerField()
#     explicit = models.BooleanField(default=False)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     album = models.ManyToManyField(Album)
    # artist = models.ManyToManyField(Artist)
    # playlist = models.ManyToManyField(Playlist)
