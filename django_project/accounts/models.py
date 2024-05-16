from django.contrib.auth.models import AbstractUser
from movies.models import Movie
from django.db import models


# Create your models here.
class User(AbstractUser):
    like_movie = models.ManyToManyField(Movie, related_name='user_like_movie')
