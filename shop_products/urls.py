from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="shop"),
    path("cart/", views.cart_page, name="cart_page"),
]