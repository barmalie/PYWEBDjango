from django.contrib import admin
from django.urls import path, include

from apps.cart_shop.urls import router as cart_router

urlpatterns = [
   path('admin/', admin.site.urls),
   path('other/cart/', include('apps.cart.urls')),
   path('other/', include('apps.common.urls')),
   #path('login/', include('apps.login.urls')),
   path('other/', include('apps.login.urls')),
   path('', include('apps.home.urls')),
   path('cart/', include('apps.cart_shop.urls')),
   path('login/', include('apps.auth_shop.urls')),
   path('api/', include(cart_router.urls)),
]