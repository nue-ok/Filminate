from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Movie


# 영화 리스트
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 영화 상세페이지(리뷰 리스트 포함)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


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


# 리뷰 검색
@api_view(['GET'])
def search_reviews(request):
    query = request.GET.get('searchStr', None)
    if query:
        reviews = Review.objects.filter(review_content__icontains=query)
    else:
        reviews = Review.objects.all()
    
    serializer = ReviewListSerializer(reviews, many=True)
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
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


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
@api_view(['PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentListSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)