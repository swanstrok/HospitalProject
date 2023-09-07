from django.contrib import admin
from .models import Patient, Department


# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'surname', 'name', 'patronymic', 'year_of_birth', 'address', 'blood_type', 'blood_rh',
        'diagnosis', 'datetime_receipt', 'datetime_discharge', 'department_id')
    list_filter = (
    'datetime_discharge', 'datetime_receipt', 'department_id', 'blood_type', 'blood_rh',
    'diagnosis')
    list_display_links = ('id', 'surname', 'department_id', 'diagnosis')
