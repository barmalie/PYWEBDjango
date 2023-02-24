from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from apps.cart_shop.models import Cart

class Login(View):
   def get(self, request):
       return render(request, "auth_shop/index_login_2.html")

   def post(self, request):
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           cart = Cart(user=user)
           if user is not None:
               login(request, user)
               return redirect('home:index')
       return redirect('auth_shop:login')

class CreateUserView(View):
   def get(self, request):
       return render(request, "auth_shop/index.html")

   def post(self, request):
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           #email = form.cleaned_data.get('email')
           password = form.cleaned_data.get('password')
           #user = User.objects.create_user(username=username, email=email, password=password)
           user = authenticate(username=username, password=password)
           cart = Cart(user=user)
           user.save()
           cart.save()
           if user is not None:
            login(request, user)
            return redirect('home:index')
       return redirect('auth_shop:login')

