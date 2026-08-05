from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = "__all__"

        widgets = {
            "patient": forms.Select(attrs={
                "class": "form-select"
            }),

            "doctor": forms.Select(attrs={
                "class": "form-select"
            }),

            "appointment_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "appointment_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),

            "reason": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        doctor = cleaned_data.get("doctor")
        date = cleaned_data.get("appointment_date")
        time = cleaned_data.get("appointment_time")

        if doctor and date and time:

            exists = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=date,
                appointment_time=time
            )

            if self.instance.pk:
                exists = exists.exclude(pk=self.instance.pk)

            if exists.exists():
                raise forms.ValidationError(
                    "This doctor already has an appointment at this date and time."
                )

        return cleaned_data