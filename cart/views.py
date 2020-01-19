from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = int(cart.get(id, quantity))

    cart_p = request.session['cart'] = cart
    print("This is cart : ", cart)
    return redirect(reverse('view_cart'))
    

def adjust_cart(request, id):
    """ Adjust the quantity of an item in the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0 :
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

