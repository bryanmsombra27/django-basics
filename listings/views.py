from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by(
        "-list_date").filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {
        'listings': paged_listings
    })


def search(request):
    return render(request, 'listings/search.html')


def listing(request,  listing_id):
    # listing = Listing.objects.first(id=listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)

    return render(request, 'listings/listing.html', {
        "listing": listing
    })
