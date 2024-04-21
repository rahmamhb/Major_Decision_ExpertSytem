from django.urls import path

from . import views

urlpatterns = [
    path("api/save_form_data/", views.save_form_data, name="save_form_data"),
]