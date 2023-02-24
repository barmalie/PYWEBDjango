from django.urls import path
from .views import ViewWishListItem, ViewWishListAdd, ViewWishListDel

app_name = 'wishlist'

urlpatterns = [
    path('', ViewWishListItem.as_view(), name='wishlist'),
    path('add_wishlist/<int:product_id>', ViewWishListAdd.as_view(), name='add_to_wishlist'),
    path('del_wishlist/<int:item_id>', ViewWishListDel.as_view(), name='del_from_wishlist'),

]
