from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Bill
from .forms import BillForm


@login_required
def bill_list(request):

    query = request.GET.get("q", "")

    bills = Bill.objects.select_related(
        "appointment",
        "appointment__patient",
        "appointment__doctor"
    )

    if query:

        bills = bills.filter(

            Q(appointment__patient__first_name__icontains=query) |
            Q(appointment__patient__last_name__icontains=query) |
            Q(appointment__doctor__first_name__icontains=query) |
            Q(payment_status__icontains=query)

        )

    paginator = Paginator(bills, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "billing/bill_list.html", {
        "page_obj": page_obj,
        "query": query,
    })


@login_required
def add_bill(request):

    if request.method == "POST":

        form = BillForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Bill generated successfully."
            )

            return redirect("bill_list")

    else:

        form = BillForm()

    return render(request, "billing/bill_form.html", {
        "form": form
    })


@login_required
def edit_bill(request, id):

    bill = get_object_or_404(Bill, id=id)

    if request.method == "POST":

        form = BillForm(
            request.POST,
            instance=bill
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Bill updated successfully."
            )

            return redirect("bill_list")

    else:

        form = BillForm(instance=bill)

    return render(request, "billing/bill_form.html", {
        "form": form
    })


@login_required
def delete_bill(request, id):

    bill = get_object_or_404(Bill, id=id)

    if request.method == "POST":

        bill.delete()

        messages.success(
            request,
            "Bill deleted successfully."
        )

        return redirect("bill_list")

    return render(request, "billing/delete.html", {
        "bill": bill
    })