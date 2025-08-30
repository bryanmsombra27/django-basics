
# Create your views here.
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by("-list_date").filter(
        is_published=True)[:3]

    return render(request, 'pages/index.html', {
        "listings": listings
    })


def about(request):
    realtors = Realtor.objects.all()

    mvp_realtors = realtors.filter(is_mvp=True)

    return render(request, 'pages/about.html', {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    })
