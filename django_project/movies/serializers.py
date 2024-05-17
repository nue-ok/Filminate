from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_title', 'poster_path',)


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('genre',)
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('actor_name',)
            
    genre = GenreSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('id',)
