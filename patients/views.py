from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from django.contrib import messages


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patients/patient_list.html", {
        "patients": patients
    })


@login_required
def add_patient(request):

    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Patient added successfully."
            )

            return redirect("patient_list")

    else:
        form = PatientForm()

    return render(request,
                  "patients/patient_form.html",
                  {"form": form})


@login_required
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Patient updated successfully."
)
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)

    return render(request, "patients/patient_form.html", {
        "form": form
    })


@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        patient.delete()

        messages.success(
            request,
            "Patient deleted successfully."
)
        return redirect("patient_list")

    return render(request, "patients/delete.html", {
        "patient": patient
    })