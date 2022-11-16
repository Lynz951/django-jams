from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.FloatField()
    num_of_plays = models.IntegerField()
    explicit = models.BooleanField(default=False)
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # album = models.ManyToManyField(Album, on_delete=model.CASCADE)
    # artist = models.ManyToManyField(Artist, on_delete=model.CASCADE)
    # playlist = models.ManyToManyField(Playlist, on_delete=model.CASCADE)

class Album(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField()

# class Genre(models.Model):
#     genre = models.CharField(max_length=100)


