from rest_framework import serializers
from .models import *
from django.conf import settings


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('created_at', 'updated_at',)
        read_only_fields = ('user', 'review',)


class ReviewListSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at',)
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at',)
        read_only_fields = ('user', 'movie',)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_title', 'poster_path', 'release_date', 'countries')


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('genre',)
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('actor_name',)
    
    review_set = ReviewListSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('id',)