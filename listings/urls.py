from django.contrib import admin
from django.urls import include, path

from .views import ListingsView, ListingDetailView, SearchView

from . import views

urlpatterns = [
    path("", ListingsView.as_view(), name="listings"),
    path("<int:listing_id>", ListingDetailView.as_view(), name="listing"),
    path("search", SearchView.as_view(), name="search"),
]
