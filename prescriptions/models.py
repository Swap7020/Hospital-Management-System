from django.db import models
from appointments.models import Appointment


class Prescription(models.Model):

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescription"
    )

    diagnosis = models.TextField()

    medicines = models.TextField(
        help_text="Write one medicine per line."
    )

    dosage = models.TextField()

    instructions = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        patient = self.appointment.patient
        return f"Prescription - {patient.first_name} {patient.last_name}"