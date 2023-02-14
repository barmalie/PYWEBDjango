from django.urls import path

from .views import Login, CreateUserView

app_name = "auth_shop"

urlpatterns = [
  path('', Login.as_view(), name="login"),
  path('create/', CreateUserView.as_view(), name="create"),
]


# from django.urls import path
#
# from .views import LoginView
#
# urlpatterns = [
#    path('', LoginView.as_view()),
# ]