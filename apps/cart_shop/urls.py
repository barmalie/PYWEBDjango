from django.urls import path
from .views import ViewCart, ViewCartBuy, ViewCartAdd, ViewCartDel, CartViewSet, ViewWishListAdd, ViewWishListDel,ViewWishListItem


from rest_framework import routers

app_name = 'cart_shop'

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   #path('wishlist/'ViewWishlist.as_view(), name='wishlist'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
   #path('add_wishlist/<int:product_id>', ViewWishListAdd.as_view(), name='add_to_wishlist'),
   #path('del_wishlist/<int:item_id>',ViewWishlistDel.as_view(), name='del_from_wishlist'),
]
