from rest_framework import serializers

from patients.models import Patient
from departments.models import Department
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Bill
from prescriptions.models import Prescription


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = "__all__"