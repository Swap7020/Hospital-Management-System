from django.urls import path
from . import views

urlpatterns = [
    path("", views.prescription_list, name="prescription_list"),
    path("add/", views.add_prescription, name="add_prescription"),
    path("edit/<int:id>/", views.edit_prescription, name="edit_prescription"),
    path("delete/<int:id>/", views.delete_prescription, name="delete_prescription"),

    # PDF URL belongs here
    path("pdf/<int:id>/", views.prescription_pdf, name="prescription_pdf"),
]