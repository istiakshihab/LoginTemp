from django.shortcuts import render


def home(request):
    return render(request, 'products/home.html', {'nbar':'home'})


def profile(request):
    return render(request, 'products/profile.html', {'nbar':'profile'}, )
