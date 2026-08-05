from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "department": forms.Select(attrs={
                "class": "form-select"
            }),

            "specialization": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Specialization"
            }),

            "qualification": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Qualification"
            }),

            "experience": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Years of Experience"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "consultation_fee": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Consultation Fee"
            }),

            "is_available": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }

    def clean_experience(self):
        experience = self.cleaned_data["experience"]

        if experience < 0 or experience > 60:
            raise forms.ValidationError(
                "Experience must be between 0 and 60 years."
            )

        return experience

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if len(phone) != 10 or not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone

    def clean_consultation_fee(self):
        fee = self.cleaned_data["consultation_fee"]

        if fee <= 0:
            raise forms.ValidationError(
                "Consultation fee must be greater than 0."
            )

        return fee