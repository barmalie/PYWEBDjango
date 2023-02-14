from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product
from apps.cart_shop.views import fill_card_in_session, fill_id_card_in_session

class IndexShopView(View):

    def get(self, request):
        fill_card_in_session(request)
        fill_id_card_in_session(request)

        data = Product.objects.all()
        context = {'data': data
                   }
        return render(request, 'home/index.html', context)
       # context = {'data': [{'name': 'Bell Pepper',
       #                      'discount': 30,
       #                      'price_before': 120.00,
       #                      'price_after': 80.00,
       #                      'url': 'shop/images/product-1.jpg'},
       #                     {'name': 'Strawberry',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-2.jpg'},
       #                     {'name': 'Green Beans',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-3.jpg'},
       #                     {'name': 'Purple Cabbage',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-4.jpg'},
       #                     {'name': 'Tomatoe',
       #                      'discount': 30,
       #                      'price_before': 120.00,
       #                      'price_after': 80.00,
       #                      'url': 'shop/images/product-5.jpg'},
       #                     {'name': 'Brocolli',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-6.jpg'},
       #                     {'name': 'Carrots',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-7.jpg'},
       #                     {'name': 'Fruit Juice',
       #                      'discount': None,
       #                      'price_before': 120.00,
       #                      'url': 'shop/images/product-8.jpg'},
       #                     ]
       #            }

       #return render(request, 'home/index.html', context)