from rest_framework import serializers
from .models import *
from django.conf import settings

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_movie_count = serializers.IntegerField(source='like_movie.count', read_only=True)
    
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'profile_image', 'review_count', 'comment_count', 'like_movie_count',)
        
        
class CommentListSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review',)


class ReviewListSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
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

    similars = MovieListSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    like_count = serializers.IntegerField(source='user_like_movie.count', read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('id',)


class SimilarMovieListSerializer(serializers.ModelSerializer):
    
    choice_list = MovieListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'movie_title', 'poster_path', 'release_date', 'countries', 'choice_list',)
