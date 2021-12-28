from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    """
    A view to render the checkout form
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'The shopping cart is empty')
        return redirect(reverse('products'))
    
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JltkWJQL8Nbmp5ECJpkJLRTJ3auzBnKA5X8AbbzTlUJeDhciSq2OkFKXEo3OibZRGbbCag7kDzfNO20f4KYqV2500pblWjE8s',
        'client_secret': 'test client secret'
    }

    return render(request, 'checkout/checkout.html', context)
