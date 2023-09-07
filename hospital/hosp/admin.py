from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Patient, Department


# Register your models here.

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'surname', 'name', 'patronymic', 'year_of_birth', 'address', 'blood_type', 'blood_rh',
        'diagnosis', 'datetime_receipt', 'department_id', 'is_discharge', 'datetime_discharge', )
    list_filter = (
        'is_discharge', 'datetime_discharge', 'datetime_receipt', 'department_id', 'blood_type',
        'blood_rh', 'diagnosis')
    list_display_links = ('id', 'surname', 'department_id', 'diagnosis')
