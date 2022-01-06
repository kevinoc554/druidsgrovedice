from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


@login_required
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

@login_required
def order_history(request, order_number):
    """
    A view to return the details of a user's past order
    """
    order = get_object_or_404(Order, order_number=order_number)
    current_user = get_object_or_404(UserProfile, user=request.user)
    # Ensure logged in user cannot see another user's Order History
    if current_user != order.user_profile:
        messages.error(request, (
            'You do not have permission to view this page.')
        )
        return redirect('home')
    
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
