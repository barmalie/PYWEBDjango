from django.db import models
from apps.cart.models import Cart
from apps.cart_shop.models import Product

class ViewWishListItem(models.Model):
   wishlist = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __repr__(self):
      return f"{self.wishlist}_{self.product}"
