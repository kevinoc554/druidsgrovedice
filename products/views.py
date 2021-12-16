from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    A view to return all products, and render them on the Catalog page
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        query = request.GET['product-search']
        if not query:
            messages.error(request, 'You did not enter any search terms.')
            return redirect(reverse('products'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
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
