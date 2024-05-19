from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/<int:review_pk>/', views.review_detail),
]
