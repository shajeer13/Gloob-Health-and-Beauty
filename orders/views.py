from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .models import Order, OrderItem
from shop_products.models import Product

@login_required
def checkout(request):
    """
    Checkout view:
    - Handles session cart or single product from modal
    - Creates Order and OrderItems
    - Clears cart and redirects to order_history
    """
    cart = request.session.get('cart', [])

    # Check if modal sent a single product
    modal_product_id = request.POST.get('product_id')
    modal_qty = int(request.POST.get('quantity', 1))

    if modal_product_id:
        product = get_object_or_404(Product, id=modal_product_id)
        # Add modal product to session cart
        for item in cart:
            if item['id'] == product.id:
                item['qty'] += modal_qty
                break
        else:
            cart.append({
                'id': product.id,
                'name': product.name,
                'price': float(product.price),
                'qty': modal_qty
            })
        request.session['cart'] = cart
        request.session.modified = True

    if not cart:
        return redirect('shop')  # Redirect if cart empty

    total = sum(item['price'] * item['qty'] for item in cart)

    if request.method == 'POST':
        # Create Order + OrderItems in a transaction
        with transaction.atomic():
            order = Order.objects.create(user=request.user, total_price=total)
            for item in cart:
                product = get_object_or_404(Product, id=item['id'])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['qty'],
                    price=item['price']
                )
        # Clear session cart
        request.session['cart'] = []
        request.session.modified = True
        messages.success(request, "Order placed successfully!")
        return redirect('order_history')  # Redirect to order history page

    return render(request, 'orders/checkout.html', {'cart': cart, 'total': total})


@login_required
def order_history(request):
    """
    Displays the current user's orders
    """
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders/order_history.html', {'orders': orders})