from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def checkout(request):
    """Place order from session cart"""
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('home')

    total = sum(item['price'] * item['qty'] for item in cart)

    if request.method == 'POST':
        for item in cart:
            Order.objects.create(
                user=request.user,
                product_name=item['name'],
                quantity=item['qty'],
                price=item['price']
            )
        request.session['cart'] = []
        return redirect('order_history')

    return render(request, 'orders/checkout.html', {'cart': cart, 'total': total})

@login_required
def order_history(request):
    """Show all orders for logged-in user"""
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders/order_history.html', {'orders': orders})