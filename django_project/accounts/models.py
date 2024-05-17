from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review
from django.db import models


# Create your models here.
class User(AbstractUser):
    like_movie = models.ManyToManyField(Movie, related_name='user_like_movie')
    like_review = models.ManyToManyField(Review, related_name='user_like_review')