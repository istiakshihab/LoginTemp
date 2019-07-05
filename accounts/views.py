from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['inputPassword1'] == request.POST['inputPassword2']:
            try:
                User.objects.get(username=request.POST['InputUser'])
                return render(request,
                              'accounts/signup.html',
                              {'error': 'Username has already been taken'},
                              {'nbar': 'signup'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['InputUser'],
                                                password=request.POST['inputPassword1'],
                                                first_name=request.POST['firstName'],
                                                last_name=request.POST['lastName'],
                                                email=request.POST['emailAddress'],

                                                )
                auth.login(request, user)
                return redirect('home')
    else:
        return render(request, 'accounts/signup.html', {'nbar': 'signup'})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['InputUser'],
                                 password=request.POST['inputPassword'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Somethings Wrong!'})
    else:
        return render(request, 'accounts/login.html', {'nbar': 'login'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def trying(request):
    if request.method == 'POST':
        user = request.POST.get('InputUser')
        password = request.POST.get('inputPassword1')
        type = request.POST.get('emailAddress')

        c = Users(username=user, pasword=password, type=type)
        c.save()

        return redirect('home')
    else:
        return render(request, 'accounts/signup.html', {'nbar': 'signup'})


def trying2(request):
    if request.method == 'POST':
        user = request.POST.get('InputUser')
        password = request.POST.get('inputPassword')

        c = 'a'
        c = Users.objects.filter(username__exact=user).filter(pasword__exact=password)
        if len(c) == 0:
            print("hello")
            return redirect('home')
        else:
            print(c[0].username, c[0].pasword)
            return redirect('home')
    else:
        return render(request, 'accounts/login.html', {'nbar': 'login'})