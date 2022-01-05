from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
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
