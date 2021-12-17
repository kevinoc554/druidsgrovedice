from django.shortcuts import render
from products.models import Product


def index(request):
    """
    A view to return the Index page,
    and show the four most recently added products
    """
    products = Product.objects.all()
    length = len(products)
    products = products[length-4:length]

    context = {
        'products': products
    }

    return render(request, 'home/index.html', context)
