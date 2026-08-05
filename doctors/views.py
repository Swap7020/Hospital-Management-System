from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Doctor
from .forms import DoctorForm


@login_required
def doctor_list(request):
    query = request.GET.get("q", "")

    doctors = Doctor.objects.select_related("department").all()

    # Search functionality
    if query:
        doctors = doctors.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(department__name__icontains=query)
        )

    # Pagination (5 doctors per page)
    paginator = Paginator(doctors, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "query": query,
    }

    return render(request, "doctors/doctor_list.html", context)


@login_required
def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully.")
            return redirect("doctor_list")

    else:
        form = DoctorForm()

    return render(request, "doctors/doctor_form.html", {
        "form": form
    })


@login_required
def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor updated successfully.")
            return redirect("doctor_list")

    else:
        form = DoctorForm(instance=doctor)

    return render(request, "doctors/doctor_form.html", {
        "form": form
    })


@login_required
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":
        doctor.delete()
        messages.success(request, "Doctor deleted successfully.")
        return redirect("doctor_list")

    return render(request, "doctors/delete.html", {
        "doctor": doctor
    })