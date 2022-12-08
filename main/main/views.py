from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def production(request):
    return render(request, 'production.html')


def contacts(request):
    return render(request, 'contacts.html')

