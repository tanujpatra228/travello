from django.shortcuts import render, redirect
from landing.models import Destination
# Create your views here.


def destination(request, id):
    print('ID from destination view :> ', id)
    if request.user.is_authenticated:
        dest = Destination.objects.get(id=id)
        return render(request, "destination.html", {'dest': dest})
    else:
        login_path = '/accounts/login' + id
        print('login path in destination view:> ', login_path)
        return redirect('/accounts/login' + id)
