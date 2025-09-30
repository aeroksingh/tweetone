from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views   # <- Add this line!

urlpatterns = [
    path('admin/', admin.site.urls),
    ## path('', include('tweet.urls')),
    path('', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # <- Now it works!
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
