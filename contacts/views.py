from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get("listing_id")
        listing = request.POST.get("listing")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        user_id = request.POST.get("user_id")
        realtor_email = request.POST.get("realtor_email")

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing.")
                return redirect("/listings/" + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id, )
        # Save to database
        contact.save()
        send_mail("Property listing Inquery",
                  "There has beeen an inquery for {}. Sign into the admin panel for more info.".format(
                      listing),
                  "carolyne49@ethereal.email", [
                      realtor_email, "carolyne49@ethereal.email",
                  ],
                  fail_silently=False

                  )

        messages.success(
            request, "Your request has been submitted, we will get back to you soon!")
    return redirect("/listings/" + listing_id)
