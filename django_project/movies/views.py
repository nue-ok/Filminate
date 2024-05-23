from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Movie
from django.db.models import Q
import random

from django.contrib.auth import get_user_model
UserModel = get_user_model()


# 영화 리스트
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 추천영화 리스트
@api_view(['GET'])
def recommendations(request):
    user = get_object_or_404(UserModel, pk=request.user.id)
    # 전체영화
    all_movies = Movie.objects.all()
    all_list = list(all_movies.values_list('id', flat=True))
    # 좋아요한 영화
    like_list = user.like_movie.all()
    like_ids = list(like_list.values_list('id', flat=True))
    
    like_num = len(like_list)
    random_num = 2
    
    recommendation_list = []
    
    # 좋아요한 영화중 최대 3개 선택
    if like_num >= 3:
        print(type(like_ids), like_ids)
        recommendation_list.extend(random.sample(like_ids, 3))
    elif 0 < like_num < 3:
        recommendation_list.extend(random.sample(like_ids, like_num))
        random_num = (5 - like_num)
    else:
        random_num = 5
    
    # 좋아요한 영화의 장르들
    like_genre = []
    if like_list:
        for like in like_list: # 장르 다 합치기
            like_genre.extend(list(like.genre.all()))
    like_genre = list(set(like_genre))
    
    # 선택된 영화를 제외한 나머지 중 좋아요한 장르를 포함한 영화들
    movies = list(set(all_list) - set(recommendation_list))
    filtered_movies_id = list(all_movies.filter(Q(id__in=movies) & Q(genre__in=like_genre)).values_list('id', flat=True).distinct())

    if len(filtered_movies_id) < random_num:
        rest = list(set(movies) - set(filtered_movies_id))
        rest = random.sample(rest, random_num-len(filtered_movies_id))
        filtered_movies_id.extend(rest)
        
    # 좋아요한 영화중 추천목록
    recommendation_list = all_movies.filter(id__in=recommendation_list)
    
    # 좋아요한 영화 제외 나머지 추천목록
    random_list = random.sample(filtered_movies_id, random_num)
    random_list = all_movies.filter(id__in=random_list)
    recommendation_list = recommendation_list.union(random_list)
    
    for recommend in recommendation_list:
        re_id = list(recommend.similars.values_list('id', flat=True))
        excude_id = random.sample(re_id, 1)[0]
        recommend.choice_list = recommend.similars.exclude(id=excude_id)
        
    serializer = SimilarMovieListSerializer(recommendation_list, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# get: 영화 상세페이지(리뷰 리스트 포함), post: 영화 저장, 취소
@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        movie.is_like=True if movie in request.user.like_movie.all() else False
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if movie in request.user.like_movie.all():
            request.user.like_movie.remove(movie)
        else:
            request.user.like_movie.add(movie)
        return Response(status=status.HTTP_200_OK)


# 영화 검색
@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('searchStr', None)
    if query:
        movies_description = Movie.objects.filter(description__icontains=query)
        movies_title = Movie.objects.filter(movie_title__icontains=query)
        movies = movies_title.union(movies_description)
    else:
        movies = Movie.objects.all()
    
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 리뷰 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 상세페이지(댓글 리스트 포함) - 리뷰내용 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if request.user.id == review.user_id:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        if request.user.id == review.user_id:
            serializer = ReviewSerializer(review, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)


# 댓글 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comments(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentListSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 상세페이지(댓글은 상세조회 없음) - 댓글 수정, 삭제
@api_view(['DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.id == comment.user_id:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)