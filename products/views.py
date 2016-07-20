from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/templates/products.html", {"products": products})
