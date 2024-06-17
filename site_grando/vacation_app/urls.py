from django.urls import path
from .views import vacation_upload, vacation_upload_success, \
list_vac, vacation_edit_success, edit_vacation_status, search_vac_data, non_auth_vacation_search

app_name = 'vacation_app'

urlpatterns = [
    path('vacation_upload/', vacation_upload, name='vacation_upload'),
    path('vacation_upload_success/', vacation_upload_success, name='vacation_upload_success'),
    path('vacation_edit_success/', vacation_edit_success, name='vacation_edit_success'),
    path('vacation_list/', list_vac, name='vacation_list'),
    path('edit_vacation_status/<int:vacation_id>/', edit_vacation_status,
         name='edit_vacation_status'),
    path('vacation_search', search_vac_data, name='search_vac_data'),
    path('non_aoth_vacation_search', non_auth_vacation_search, name='non_auth_vacation_search')
]