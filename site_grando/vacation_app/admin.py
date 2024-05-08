from django.contrib import admin
from .models import VacationModel


@admin.register(VacationModel)
class VacationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'vacation_date_start', 'vacation_date_end', 'vacation_file']
    search_fields = ['name']
    save_on_top = True
