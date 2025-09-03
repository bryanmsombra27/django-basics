from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombre")
    last_name = forms.CharField(
        max_length=150, required=True, label="Apellido")
    username = forms.CharField(max_length=150, required=True, label="Usuario")
    email = forms.EmailField(required=True, label="Correo")
    password = forms.CharField(
        widget=forms.PasswordInput, required=True, label="Contraseña")
    password2 = forms.CharField(
        widget=forms.PasswordInput, required=True, label="Confirmar contraseña")

    def clean(self):
        return super().clean()
