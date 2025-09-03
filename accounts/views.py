from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.views.generic import ListView, View
# Create your views here.
from .form import RegisterForm


class RegisterView(View):

    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        data = RegisterForm(request.POST)

        if data.is_valid():
            data = data.cleaned_data
            if data["password"] == data["password2"]:
                if User.objects.filter(username=data["username"]).exists():
                    messages.error(request, "username already exists")
                    return redirect("register")
                else:
                    if User.objects.filter(email=data["email"]).exists():
                        messages.error(request, "email already exists")
                        return redirect("register")
                    else:
                        user = User.objects.create_user(
                            username=data["username"], password=data["password"], email=data["email"], first_name=data["first_name"], last_name=data["last_name"])
                        # LOGIN USER AFTER REGISTER
                        # auth.login(request, user)
                        # messages.success(request, "you are now logged in")
                        # return redirect("index")
                        user.save()
                        messages.success(
                            request, "You are now registered and can log in")
                        return redirect("login")
            else:
                messages.error(request, "passwords does not match")
                return redirect("register")


def register(request):

    if request.method == 'POST':
        # get form values
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        # check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # LOGIN USER AFTER REGISTER
                    # auth.login(request, user)
                    # messages.success(request, "you are now logged in")
                    # return redirect("index")
                    user.save()
                    messages.success(
                        request, "You are now registered and can log in")
                    return redirect("login")
        else:
            messages.error(request, "passwords does not match")
            return redirect("register")
    else:
        return render(request, 'accounts/register.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "invalid credentials")
            return redirect("login")


class HomeDashboardView(ListView):
    model = Contact
    template_name = "accounts/dashboard.html"
    context_object_name = "contacts"

    def get_queryset(self):
        return super().get_queryset().order_by("-contact_date").filter(user_id=self.request.user.id)


class AuthView(View):
    def get(self, request):
        pass

    def post(self, request):
        auth.logout(request)
        messages.success(request, "you are now logged out")
        return redirect("index")
