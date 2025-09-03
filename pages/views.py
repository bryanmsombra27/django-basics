
# Create your views here.
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
from django.views.generic import ListView


class HomeView(ListView):
    model = Listing
    template_name = "pages/index.html"
    context_object_name = "listings"

    def get_queryset(self):
        return super().get_queryset().order_by("-list_date").filter(is_published=True)[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price_choices"] = price_choices
        context["bedroom_choices"] = bedroom_choices
        context["state_choices"] = state_choices
        return context


class AboutView(ListView):
    model = Realtor
    template_name = "pages/about.html"
    context_object_name = "realtors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mvp_realtors"] = Realtor.objects.all().filter(is_mvp=True)
        return context
