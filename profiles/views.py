from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    """
    A view to return the user's profile page
    """
    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery information updated.')

    orders = userprofile.orders.all()
    form = UserProfileForm(instance=userprofile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'do_not_show_cart': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    """
    A view to return the details of a user's past order
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is the order details for Order Number: {order_number}. '
        'A confirmation email was sent at the time of ordering')
        )
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
