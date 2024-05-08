from django.urls import path
from .views import vacation_upload, vacation_upload_success

app_name = 'vacation_app'

urlpatterns = [
    path('vacation_upload/', vacation_upload, name='vacation_upload'),
    path('vacation_upload_success/', vacation_upload_success, name='vacation_upload_success')
]