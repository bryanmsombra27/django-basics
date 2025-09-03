from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from .choices import price_choices, bedroom_choices, state_choices
from django.views.generic import ListView, DetailView


class ListingsView(ListView):
    model = Listing
    template_name = "listings/listings.html"
    context_object_name = "listings"
    ordering = ["-list_date"]
    paginate_by = 3

    def get_queryset(self):
        return Listing.objects.filter(is_published=True).order_by("-list_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sobrescribimos listings para que sea el objeto Page
        context["listings"] = context["page_obj"]
        return context


class SearchView(ListView):
    model = Listing
    template_name = "listings/search.html"
    context_object_name = "listings"
    ordering = ["-list_date"]

    def get_queryset(self):
        queryset = Listing.objects.order_by("-list_date")
        params = self.request.GET

        keywords = params.get("keywords")
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

        city = params.get("city")
        if city:
            queryset = queryset.filter(city__iexact=city)

        state = params.get("state")
        if state:
            queryset = queryset.filter(state__iexact=state)

        bedrooms = params.get("bedrooms")
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)

        price = params.get("price")
        if price:
            queryset = queryset.filter(price__lte=price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price_choices"] = price_choices
        context["bedroom_choices"] = bedroom_choices
        context["state_choices"] = state_choices
        context["values"] = self.request.GET.dict()
        return context


class ListingDetailView(DetailView):
    queryset = Listing.objects.all()
    context_object_name = "listing"
    template_name = "listings/listing.html"
    pk_url_kwarg = "listing_id"
