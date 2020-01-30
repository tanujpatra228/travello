from django.urls import path, re_path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    re_path(r"login(?P<id>\d+)", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
