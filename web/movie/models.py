from django.db import models

# Create your models here.

class movieSlice(models.Model):
    name = models.CharField(max_length = 500)
    abstract = models.CharField(max_length = 10000)
    picUrl = models.CharField(max_length = 500)

class comment(models.Model):
    content = models.CharField(max_length = 1000)
    movie = models.ForeignKey(movieSlice, on_delete = models.CASCADE)

class actor(models.Model):
    name = models.CharField(max_length = 100)
    abstract = models.CharField(max_length = 10000)
    picUrl = models.CharField(max_length = 500)

class connect(models.Model):
    movieId = models.IntegerField()
    actorId = models.IntegerField()