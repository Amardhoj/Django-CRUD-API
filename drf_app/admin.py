from django.contrib import admin
from drf_app.models import Employee, Department

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)