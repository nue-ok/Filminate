from django.db import models
from django.conf import settings


# Create your models here.
class Director(models.Model):
    director_name = models.CharField(max_length=20)


class Genre(models.Model):
    genre = models.CharField(max_length=20)


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    
    movie_title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    poster_path = models.TextField()
    running_time = models.IntegerField()
    release_date = models.DateTimeField()
    is_adult = models.BooleanField()

    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_like')
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    actor = models.ManyToManyField(Actor, related_name='movie_actor')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    review_content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='review_like')
    
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    comment_content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)