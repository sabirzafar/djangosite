from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the djangosite home page.")


def about(request):
    return HttpResponse("Hello, world. You're at the djangosite about page.")


def contact(request):
    return HttpResponse("Hello, world. You're at the djangosite contact page.")
