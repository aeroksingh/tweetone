from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),    # Add
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),    # Edit
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Delete
    path('register/', views.register, name='register'),
]
