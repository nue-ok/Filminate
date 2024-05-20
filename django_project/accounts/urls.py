from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.index),
    path('<str:username>/like_movies/', views.like_movies),
    path('<str:username>/my_reviews/', views.my_reviews),
    path('<str:username>/my_comments/', views.my_comments),
    path('<str:username>/update/', views.update_user),
    path('<str:username>/delete/', views.delete_user),
]
