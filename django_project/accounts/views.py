from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *
UserModel = get_user_model()


#마이페이지(유저 정보)
@api_view(['GET'])
def index(request, username):
    user = get_object_or_404(UserModel, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저가 저장한 영화 리스트
@api_view(['GET'])
def like_movies(request, username):
    user = get_object_or_404(UserModel, username=username)
    like_movies = user.like_movie.all()
    serializer = MovieListSerializer(like_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저 리뷰 리스트
@api_view(['GET'])
def my_reviews(request, username):
    user = get_object_or_404(UserModel, username=username)
    my_reviews = user.review_set.all()
    serializer = ReviewListSerializer(my_reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저 댓글 리스트
@api_view(['GET'])
def my_comments(request, username):
    user = get_object_or_404(UserModel, username=username)
    my_comments = user.comment_set.all()
    serializer = CommentListSerializer(my_comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 회원정보 수정
@api_view(['PUT'])
def update_user(request):
    serializer = UserUpdateSerializer(data=request.data, instance=request.user)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# 회원탈퇴
@api_view(['DELETE'])
def delete_user(request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    