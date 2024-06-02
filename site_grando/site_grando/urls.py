from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacation/', include('vacation_app.urls'), name='vacation_upload'),
    path('users/', include('users.urls'), name='users'),
    path('news/', include('news_app.urls'), name='news'),
    path('about/', include('about_app.urls'), name='about'),
    path('grando-main-page/', index, name='index')
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)