from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),      # /orders/checkout/
    path('history/', views.order_history, name='order_history'),  # /orders/history/
]