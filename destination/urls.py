from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r"place(?P<id>\d+)$", views.destination, name="destination"),
]
