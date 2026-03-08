from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from shop_products.models import Product

# 🏠 Shop page (after login/signup)
@login_required
def home(request):
    """Display all products"""
    products = Product.objects.all()
    return render(request, 'accounts/product_list.html', {'products': products})

# 📝 Signup
def signup_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop')  # redirect to shop after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 🔑 Login
def login_view(request):
    """User login view"""
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop')  # redirect to shop after login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# 🛒 Cart page
@login_required
def cart_view(request):
    """Display current cart from session"""
    cart = request.session.get('cart', [])
    total = sum(item['price'] * item['qty'] for item in cart)
    return render(request, 'accounts/cart.html', {'cart': cart, 'total': total})

# ➕ Add product to cart
@login_required
def add_to_cart(request, product_id):
    """Add a product to the cart (stored in session)"""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])

    for item in cart:
        if item['id'] == product.id:
            item['qty'] += 1
            break
    else:
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'qty': 1
        })

    request.session['cart'] = cart
    return redirect('shop')

# ➖ Remove item from cart
@login_required
def remove_from_cart(request, product_id):
    """Remove a product from the session cart"""
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    request.session['cart'] = cart
    return redirect('cart')

# 👤 Profile page
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# 🚪 Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')