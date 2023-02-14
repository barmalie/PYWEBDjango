from django.urls import path
from .views import ViewCart, ViewCartBuy, ViewWishlist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('wishlist/'ViewWishlist.as_view(), name='wishlist'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
]
