from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('cart/', include('apps.cart.urls')),
   path('', include('apps.common.urls')),
   #path('login/', include('apps.login.urls')),
   path('', include('apps.login.urls')),
]