from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.views import View
from .contact_form import ContactForm

# Create your views here.


class ContactView(View):

    def get(self, request):
        pass

    def post(self, request):
        contact = ContactForm(request.POST)
        realtor_email = request.POST.get("realtor_email")

        if request.user.is_authenticated:
            # ES IMPORTANTE HACER EL COMMIT EN FALSE, SI SE QUIERE MANIPULAR LA INFORMACION DEL FORMULARIO
            contact = contact.save(commit=False)

        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(
            listing_id=str(contact.listing_id), user_id=user_id)
        if has_contacted:
            messages.error(
                request, "You have already made an inquiry for this listing.")
            return redirect("/listings/" + str(contact.listing_id))
        contact.save()
        send_mail("Property listing Inquery",
                  "There has beeen an inquery for {}. Sign into the admin panel for more info.".format(
                      contact.listing),
                  "carolyne49@ethereal.email", [
                      realtor_email, "carolyne49@ethereal.email",
                  ],
                  fail_silently=False

                  )
        messages.success(
            request, "Your request has been submitted, we will get back to you soon!")
        return redirect("/listings/" + str(contact.listing_id))
