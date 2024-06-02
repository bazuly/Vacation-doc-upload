from django.contrib import admin
from .models import AboutEmployeeModel, JobModel, ReferenceBookModel

admin.site.register(AboutEmployeeModel)
admin.site.register(JobModel)
admin.site.register(ReferenceBookModel)
