from django.shortcuts import render

# Create your views here.


def shop(request):
    # return HttpResponse("Hello, world. You're at the djangosite home page.")
    return render(request, 'shop/products.html')
