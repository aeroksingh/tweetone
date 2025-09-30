
from django.contrib import admin
from django.urls import path, include  # <-- make sure 'path' is imported here
from django.conf import settings
from django.conf.urls.static import static
from . import views  # ✅ This is the correct one!



urlpatterns = [
    
    path('', views.tweet_list, name='tweet_list'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    path('tweet/edit/<int:id>/', views.tweet_edit, name='tweet_edit'),
    path('tweet/delete/<int:id>/', views.tweet_delete, name='tweet_delete'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
