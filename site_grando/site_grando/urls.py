from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacation/', include('vacation_app.urls'), name='vacation_upload'),
    path('users/', include('users.urls'), name='users'),
    path('news/', include('news_app.urls'), name='news')
]
