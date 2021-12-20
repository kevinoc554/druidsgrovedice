from django.shortcuts import render


def view_cart(request):
    """
    A view to return and display the contents of the user's shopping cart
    """
    return render(request, 'cart/shopping_cart.html')
