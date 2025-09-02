from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.


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


def login(request):
    if request.method == 'POST':
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
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    # user = get_object_or_404(Contact,)
    user_contacts = Contact.objects.order_by(
        "-contact_date").filter(user_id=request.user.id)
    return render(request, 'accounts/dashboard.html', {
        "contacts": user_contacts
    })


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "you are now logged out")
        return redirect("index")
