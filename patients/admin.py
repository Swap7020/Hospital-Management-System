from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'age',
        'gender',
        'phone',
        'email',
    )

    search_fields=(
        'first_name',
        'last_name',
        'phone',
        'email',
    )

    list_filter = (
        'gender',
        'created_at',
    )

    ordering = ('id',
    )