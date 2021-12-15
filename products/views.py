from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    A view to return the details of an individual product, and render them
    on the product's page
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
