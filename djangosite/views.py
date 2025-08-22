from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("Hello, world. You're at the djangosite home page.")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("Hello, world. You're at the djangosite about page.")
    return render(request, 'website/about.html')


def contact(request):
    # return HttpResponse("Hello, world. You're at the djangosite contact page.")
    return render(request, 'website/contact.html')
