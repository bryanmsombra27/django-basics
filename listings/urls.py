from django.contrib import admin
from django.urls import include, path

from .views import ListingsView

from . import views

urlpatterns = [
    # path("", views.index, name="listings"),
    path("", ListingsView.as_view(), name="listings"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("search", views.search, name="search"),
]
