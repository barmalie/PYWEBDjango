from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('cart/', include('apps.cart.urls')),
   path('', include('apps.common.urls')),
   path('', include('apps.test_app.urls')),
   path('', include('apps.login.urls')),
]