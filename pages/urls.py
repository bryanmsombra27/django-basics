from django.urls import include, path

from . import views
from .views import HomeView, AboutView

urlpatterns = [
    # path("", views.index, name="index"),
    path("", HomeView.as_view(), name="index"),
    path("about", AboutView.as_view(), name="about"),
]
