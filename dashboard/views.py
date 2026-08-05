from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from patients.models import Patient
from doctors.models import Doctor
from departments.models import Department
from appointments.models import Appointment


@login_required
def dashboard(request):

    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_departments = Department.objects.count()
    total_appointments = Appointment.objects.count()

    today = timezone.now().date()

    today_appointments = Appointment.objects.filter(
        appointment_date=today
    ).select_related(
        "patient",
        "doctor"
    )

    recent_patients = Patient.objects.order_by("-id")[:5]

    recent_doctors = Doctor.objects.order_by("-id")[:5]

    context = {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_departments": total_departments,
        "total_appointments": total_appointments,
        "today_appointments": today_appointments,
        "recent_patients": recent_patients,
        "recent_doctors": recent_doctors,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )