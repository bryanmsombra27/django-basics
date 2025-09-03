from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("contact", views.ContactView.as_view(), name="contact")
    # path("contact", views.contact, name="contact")
]
