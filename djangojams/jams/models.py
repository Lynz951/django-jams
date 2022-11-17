from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=1000)

class Album(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField()

class Playlist(models.Model):
    title = models.CharField(max_length=100)

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.FloatField()
    num_of_plays = models.IntegerField()
    explicit = models.BooleanField(default=False)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)
    album = models.ManyToManyField('Album')
    artist = models.ManyToManyField('Artist')
    playlist = models.ManyToManyField('Playlist')


    def __str__(self):
        return self.title + ": " + self.genre + ". By:" + self.artist

 

   









