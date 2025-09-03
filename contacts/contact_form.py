from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["contact_date"]
        fields = [
            "name",
            "email",
            "phone",
            "message",
            "listing",
            "listing_id",
            "user_id"
        ]
        labels = {
            "name": "Tu nombre",
            "email": "Tu correo",
            "phone": "Tu telefono",
            "message": "Mensaje"
        }
