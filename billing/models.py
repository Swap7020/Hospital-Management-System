from django.db import models
from appointments.models import Appointment


class Bill(models.Model):

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="bill"
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    medicine_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    laboratory_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # 👇 Replace your existing save() method with this
    def save(self, *args, **kwargs):

        # Automatically get doctor's consultation fee
        if self.appointment:
            self.consultation_fee = self.appointment.doctor.consultation_fee

        # Calculate total bill
        self.total_amount = (
            self.consultation_fee +
            self.medicine_charge +
            self.laboratory_charge +
            self.other_charge
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.id}"