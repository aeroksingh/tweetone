from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet import views  # ✅ valid if 'views.py' exists inside the 'tweet' app


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('tweet.urls')),  # all your app's views
#     path('accounts/', include('django.contrib.auth.urls')),  # default auth views
#       # custom logout
# ]


urlpatterns = [
    path('', include('tweet.urls')),  # your main app views accessible to all
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    # path('signup/', views.signup_view, name='signup'),  # custom signup
    path('logout/', views.logout_view, name='logout'),

    path('login/', views.login_view, name='login'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
