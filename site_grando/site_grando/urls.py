from django.contrib import admin
from django.urls import path, include
from vacation_app.views import VacationForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vacation_app.urls'), name='vacation_upload')
]
