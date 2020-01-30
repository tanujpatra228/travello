from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used! Want to <a href="accounts/login">Login</a>?')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username,
                                                password=password1)
                user.save()
                messages.success(request, 'user created')
                return redirect('login')
        else:
            messages.warning(request, 'Password must be same')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request, id=0):
    print('ID in login view :>', id)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not (User.objects.filter(username=username).exists()):
            messages.error(request, 'Username not registered yet! Want to <a href="accounts/register">Register</a>?')
            return redirect('login', id)

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            if id is not '0':      # user will redirected to the desired destination page
                print('id > 0 = true')
                return redirect('/destination/place' + id)

            else:
                print('id > 0 = true')
                return redirect('/')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login', id)
    else:
        return render(request, 'login.html', {'id': id})


def logout(request):
    auth.logout(request)
    return redirect('/')
