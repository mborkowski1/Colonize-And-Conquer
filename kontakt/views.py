from django.shortcuts import render

# Create your views here.


def kontakt(request):
    return render(request, 'kontakt.html')


def cookies(request):
    return render(request, 'cookies.html')


def zasady(request):
    return render(request, 'zasady.html')
