from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from shop_products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user)
    item, created = OrderItem.objects.get_or_create(order=order, product=product)
    item.quantity += 1
    item.save()
    return redirect('cart')

@login_required
def cart_view(request):
    order, created = Order.objects.get_or_create(user=request.user)
    return render(request, 'orders/cart.html', {'order': order})