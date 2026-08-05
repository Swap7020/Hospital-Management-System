from django import forms
from .models import Prescription


class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = "__all__"

        widgets = {
            "appointment": forms.Select(attrs={
                "class": "form-select"
            }),

            "diagnosis": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter diagnosis..."
            }),

            "medicines": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "One medicine per line"
            }),

            "dosage": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Example:\nParacetamol - 1 Tablet Twice Daily"
            }),

            "instructions": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Additional instructions..."
            }),
        }

    def clean(self):

        cleaned_data = super().clean()

        appointment = cleaned_data.get("appointment")

        if appointment:

            prescription = Prescription.objects.filter(
                appointment=appointment
            )

            if self.instance.pk:
                prescription = prescription.exclude(pk=self.instance.pk)

            if prescription.exists():
                raise forms.ValidationError(
                    "Prescription already exists for this appointment."
                )

        return cleaned_data