from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Appointment
from .forms import AppointmentForm


@login_required
def appointment_list(request):

    query = request.GET.get("q", "")

    appointments = Appointment.objects.select_related(
        "patient",
        "doctor"
    ).all()

    if query:
        appointments = appointments.filter(
            Q(patient__first_name__icontains=query) |
            Q(patient__last_name__icontains=query) |
            Q(doctor__first_name__icontains=query) |
            Q(doctor__last_name__icontains=query) |
            Q(status__icontains=query)
        )

    paginator = Paginator(appointments, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "query": query,
    }

    return render(
        request,
        "appointments/appointment_list.html",
        context
    )


@login_required
def add_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Appointment booked successfully."
            )

            return redirect("appointment_list")

    else:
        form = AppointmentForm()

    return render(
        request,
        "appointments/appointment_form.html",
        {
            "form": form
        }
    )


@login_required
def edit_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == "POST":

        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Appointment updated successfully."
            )

            return redirect("appointment_list")

    else:

        form = AppointmentForm(
            instance=appointment
        )

    return render(
        request,
        "appointments/appointment_form.html",
        {
            "form": form
        }
    )


@login_required
def delete_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == "POST":

        appointment.delete()

        messages.success(
            request,
            "Appointment deleted successfully."
        )

        return redirect("appointment_list")

    return render(
        request,
        "appointments/delete.html",
        {
            "appointment": appointment
        }
    )