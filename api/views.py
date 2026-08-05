from rest_framework import viewsets

from patients.models import Patient
from departments.models import Department
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Bill
from prescriptions.models import Prescription

from .serializers import (
    PatientSerializer,
    DepartmentSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    BillSerializer,
    PrescriptionSerializer,
)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("-id")
    serializer_class = PatientSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("-id")
    serializer_class = DepartmentSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("-id")
    serializer_class = DoctorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by("-id")
    serializer_class = AppointmentSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all().order_by("-id")
    serializer_class = BillSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().order_by("-id")
    serializer_class = PrescriptionSerializer