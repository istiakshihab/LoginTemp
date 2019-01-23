from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


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
