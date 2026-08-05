from django import forms
from .models import Bill


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill

        # Hide auto-calculated fields
        exclude = ["consultation_fee", "total_amount"]

        widgets = {
            "appointment": forms.Select(attrs={
                "class": "form-select"
            }),

            "medicine_charge": forms.NumberInput(attrs={
                "class": "form-control",
                "value": 0
            }),

            "laboratory_charge": forms.NumberInput(attrs={
                "class": "form-control",
                "value": 0
            }),

            "other_charge": forms.NumberInput(attrs={
                "class": "form-control",
                "value": 0
            }),

            "payment_status": forms.Select(attrs={
                "class": "form-select"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        appointment = cleaned_data.get("appointment")

        if appointment:
            bill = Bill.objects.filter(appointment=appointment)

            if self.instance.pk:
                bill = bill.exclude(pk=self.instance.pk)

            if bill.exists():
                raise forms.ValidationError(
                    "A bill already exists for this appointment."
                )

        return cleaned_data