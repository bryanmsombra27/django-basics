from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.all().order_by(
        "-list_date").filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {
        'listings': paged_listings,

    })


def search(request):
    queryset_list = Listing.objects.order_by("-list_date")

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get("keywords")
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET.get("city")
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # state
    if 'state' in request.GET:
        state = request.GET.get("state")
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get("bedrooms")
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # price
    if 'price' in request.GET:
        price = request.GET.get("price")
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    return render(request, 'listings/search.html', {
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "listings": queryset_list,
        "values": request.GET
    })


def listing(request,  listing_id):
    # listing = Listing.objects.first(id=listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)

    return render(request, 'listings/listing.html', {
        "listing": listing
    })
