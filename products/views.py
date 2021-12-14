from django.shortcuts import render
from .models import Product

def all_products(request):
    """
    A view to return all products, and render them on the Catalog page
    """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product.html', context)
