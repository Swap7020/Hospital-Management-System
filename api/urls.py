from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PatientViewSet,
    DepartmentViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    BillViewSet,
    PrescriptionViewSet,
)

router = DefaultRouter()

router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"departments", DepartmentViewSet, basename="departments")
router.register(r"doctors", DoctorViewSet, basename="doctors")
router.register(r"appointments", AppointmentViewSet, basename="appointments")
router.register(r"billing", BillViewSet, basename="billing")
router.register(r"prescriptions", PrescriptionViewSet, basename="prescriptions")

urlpatterns = [
    path("", include(router.urls)),
]