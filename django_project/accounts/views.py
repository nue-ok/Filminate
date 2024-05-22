from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect, HttpResponse
import requests

from .serializers import *
from .models import *
UserModel = get_user_model()


# 구글 로그인
def googlelogin(request):
    response = requests.get('http://127.0.0.1:8000/accounts/google/login/')
    print(response.headers['Location'])
    if response.status_code // 100 == 3:  # HTTP 상태 코드가 3XX인 경우
        # 새로운 위치로 리디렉션
        new_location = response.headers['Location']
        print('sdfsfsdfsd')
        print(new_location)
        return HttpResponse({'redirection': new_location})
    # else:
    #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
def do_login(request):
    # 요청(request)에서 세션 ID 가져오기
    session_key = request.session.session_key
    # 세션 ID를 기반으로 세션을 가져옴
    session = Session.objects.get(session_key=session_key)
    # 세션에서 사용자 정보를 가져옴
    user_id = session.get_decoded().get('_auth_user_id')
    # 사용자 ID를 기반으로 토큰을 생성하여 반환
    token, _ = Token.objects.get_or_create(user_id=user_id)
    return Response({'key': token.key}, status=status.HTTP_200_OK)


#마이페이지(유저 정보)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request, username):
    user = get_object_or_404(UserModel, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저가 저장한 영화 리스트
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def like_movies(request, username):
    user = get_object_or_404(UserModel, username=username)
    like_movies = user.like_movie.all()
    serializer = MovieListSerializer(like_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저 리뷰 리스트
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_reviews(request, username):
    user = get_object_or_404(UserModel, username=username)
    my_reviews = user.review_set.all()
    serializer = ReviewListSerializer(my_reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 유저 댓글 리스트
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_comments(request, username):
    user = get_object_or_404(UserModel, username=username)
    my_comments = user.comment_set.all()
    serializer = CommentListSerializer(my_comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 회원정보 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, username):
    user = get_object_or_404(UserModel, username=username)
    if request.user == user:
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


# 회원탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, username):
    user = get_object_or_404(UserModel, username=username)
    if request.user == user:
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


def kakao_test(request):
    return render(request, 'kakao.html')
    