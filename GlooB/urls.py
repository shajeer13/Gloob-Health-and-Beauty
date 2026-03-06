from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root URL → Sign Up page
    path('', account_views.signup_view, name='signup'),

    # Accounts URLs → login/signup/cart
    path('accounts/', include('accounts.urls')),

    # Shop page → after login/signup
    path('shop/', account_views.home, name='shop'),
]