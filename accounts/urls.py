from django.urls import path
from django.conf.urls.i18n import set_language
from . import views
from orders import views as orders_views   # add this line

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    # language change
    path('set-language/', set_language, name='set_language'),

    # ✅ Checkout route from orders app
    path('checkout/', orders_views.checkout, name='checkout'),
    path('order-history/', orders_views.order_history, name='order_history'),
]