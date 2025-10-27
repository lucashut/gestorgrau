from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.templatetags.static import static
from .models import Product
from json import dumps, loads


# Create your views here.
def home(request):
    img_url = static('assets/icone.png')
    return render(request, 'home.html', {"img_url": img_url})


def inspector(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def search(request):
    if request.method == "POST":
        try:
            sku_code = request.POST.get("sku")
            product = Product.objects.get( sku=sku_code )

            pinfo = {
                "name": product.name,
                "price": product.price
            }

            return render(request, "search.html", {"product": pinfo})
        
        except Product.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Produto não encontrado")


    return render(request, "search.html")