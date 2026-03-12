from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.signup_view, name='signup'),
    path('accounts/', include('accounts.urls')),
    path('shop/', shop_views.shop_index, name='shop'),  # <-- Shop URL
    path('orders/', include('orders.urls')),
]