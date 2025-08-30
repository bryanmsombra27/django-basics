from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by("-list_date")
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {
        'listings': paged_listings
    })


def search(request):
    return render(request, 'listings/search.html')


def listing(request,  listing_id):
    return render(request, 'listings/listing.html')
