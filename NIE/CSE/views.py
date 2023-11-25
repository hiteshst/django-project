from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def product(request):
    return render(request, 'product.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def base(request):
    return render(request, 'base.html')
