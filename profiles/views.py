from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    A view to return the user's profile page
    """
    userprofile = get_object_or_404(UserProfile, user=request.user)
    orders = userprofile.orders.all()
    form = UserProfileForm(instance=userprofile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
