from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "appointment",
        "consultation_fee",
        "total_amount",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "payment_status",
        "created_at",
    )

    search_fields = (
        "appointment__patient__first_name",
        "appointment__patient__last_name",
        "appointment__doctor__first_name",
        "appointment__doctor__last_name",
    )

    ordering = ("-created_at",)