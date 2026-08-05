from django.contrib import admin
from .models import Doctor
# Doctor model will be added later


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
        "department",
        "specialization",
        "qualification",
        "experience",
        "phone",
        "email",
        "consultation_fee",
        "is_available",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "specialization",
        "qualification",
        "phone",
        "email",
    )

    list_filter = (
        "department",
        "gender",
        "is_available",
        "created_at",
    )

    ordering = (
        "first_name",
        "last_name",
    )

    list_per_page = 10