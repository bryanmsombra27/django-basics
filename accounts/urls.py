from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.AuthView.as_view(), name="logout"),
    path("dashboard", views.HomeDashboardView.as_view(), name="dashboard"),
]
