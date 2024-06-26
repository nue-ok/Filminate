from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=20)
    genre_code = models.IntegerField()


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    actor_code = models.IntegerField()


class Movie(models.Model):
    director = models.CharField(max_length=50)
    
    movie_title = models.CharField(max_length=100)
    description = models.TextField()
    poster_path = models.TextField()
    running_time = models.IntegerField()
    release_date = models.CharField(max_length=4)
    countries = models.CharField(max_length=100)
    certification = models.CharField(max_length=10)
    movie_code = models.IntegerField()
    
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    actor = models.ManyToManyField(Actor, related_name='movie_actor')
    
    similars = models.ManyToManyField('self', symmetrical=False, related_name='movie_similars')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    review_content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    comment_content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)