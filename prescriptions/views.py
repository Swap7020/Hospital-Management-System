from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Prescription
from .forms import PrescriptionForm

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


@login_required
def prescription_list(request):

    query = request.GET.get("q", "")

    prescriptions = Prescription.objects.select_related(
        "appointment",
        "appointment__patient",
        "appointment__doctor"
    ).order_by("-created_at")

    if query:
        prescriptions = prescriptions.filter(
            Q(appointment__patient__first_name__icontains=query) |
            Q(appointment__patient__last_name__icontains=query) |
            Q(appointment__doctor__first_name__icontains=query) |
            Q(diagnosis__icontains=query)
        )

    paginator = Paginator(prescriptions, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "prescriptions/prescription_list.html", {
        "page_obj": page_obj,
        "query": query
    })


@login_required
def add_prescription(request):

    if request.method == "POST":

        form = PrescriptionForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Prescription added successfully."
            )

            return redirect("prescription_list")

    else:
        form = PrescriptionForm()

    return render(request, "prescriptions/prescription_form.html", {
        "form": form
    })


@login_required
def edit_prescription(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    if request.method == "POST":

        form = PrescriptionForm(
            request.POST,
            instance=prescription
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Prescription updated successfully."
            )

            return redirect("prescription_list")

    else:

        form = PrescriptionForm(instance=prescription)

    return render(request, "prescriptions/prescription_form.html", {
        "form": form
    })


@login_required
def delete_prescription(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    if request.method == "POST":

        prescription.delete()

        messages.success(
            request,
            "Prescription deleted successfully."
        )

        return redirect("prescription_list")

    return render(request, "prescriptions/delete.html", {
        "prescription": prescription
    })

@login_required
def prescription_pdf(request, id):

    prescription = get_object_or_404(Prescription, id=id)

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        f'attachment; filename="Prescription_{prescription.id}.pdf"'
    )

    pdf = canvas.Canvas(response)

    width, height = pdf._pagesize

    y = height - 50

    # Hospital Name
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(width / 2, y, "CITY HOSPITAL")

    y -= 20

    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(
        width / 2,
        y,
        "Hospital Management System"
    )

    y -= 40

    pdf.line(40, y, width - 40, y)

    y -= 30

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y, "Prescription")

    y -= 30

    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        40,
        y,
        f"Prescription ID : {prescription.id}"
    )

    y -= 20

    pdf.drawString(
        40,
        y,
        f"Date : {prescription.created_at.strftime('%d-%m-%Y')}"
    )

    y -= 30

    patient = prescription.appointment.patient

    doctor = prescription.appointment.doctor

    pdf.drawString(
        40,
        y,
        f"Patient : {patient.first_name} {patient.last_name}"
    )

    y -= 20

    pdf.drawString(
        40,
        y,
        f"Age : {patient.age}"
    )

    y -= 20

    pdf.drawString(
        40,
        y,
        f"Gender : {patient.gender}"
    )

    y -= 30

    pdf.drawString(
        40,
        y,
        f"Doctor : Dr. {doctor.first_name} {doctor.last_name}"
    )

    y -= 20

    pdf.drawString(
        40,
        y,
        f"Department : {doctor.department}"
    )

    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(40, y, "Diagnosis")

    y -= 20

    pdf.setFont("Helvetica", 11)
    pdf.drawString(40, y, prescription.diagnosis)

    y -= 40

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(40, y, "Medicines")

    y -= 20

    pdf.setFont("Helvetica", 11)

    for medicine in prescription.medicines.split("\n"):

        pdf.drawString(60, y, "• " + medicine)

        y -= 18

    y -= 15

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(40, y, "Dosage")

    y -= 20

    pdf.setFont("Helvetica", 11)

    for dosage in prescription.dosage.split("\n"):

        pdf.drawString(60, y, dosage)

        y -= 18

    y -= 15

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(40, y, "Instructions")

    y -= 20

    pdf.setFont("Helvetica", 11)

    if prescription.instructions:

        for line in prescription.instructions.split("\n"):

            pdf.drawString(60, y, line)

            y -= 18

    y -= 50

    pdf.line(width - 200, y, width - 40, y)

    y -= 20

    pdf.drawString(width - 180, y, "Doctor Signature")

    pdf.save()

    return response