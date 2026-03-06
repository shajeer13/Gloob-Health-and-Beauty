from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),           # signup/login
    path('shop/', include('shop_products.urls')), # shop pages
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ഈ ഭാഗം ആവശ്യമില്ല, duplicate ആണ്
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # signup/login etc.
    path('shop/', include('shop_products.urls')),  # <--- include shop URLs
]