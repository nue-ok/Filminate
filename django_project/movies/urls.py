from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/search/', views.search_movies),
    
    path('reviews/<int:movie_pk>/create/', views.create_review),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/search/', views.search_reviews),
    
    path('comments/<int:review_pk>/create/', views.create_comments),
    path('comments/<int:comment_pk>/', views.comment_detail),
    
    path('movies/recommendations/', views.recommendations),
]
