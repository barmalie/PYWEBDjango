from django.urls import path

from .views import CurrentDateView, IndexView

urlpatterns = [
   path('', IndexView.as_view()),
   path('login/', CurrentDateView.as_view()), # создается маршрут, который связывает url datetime/ и представление  CurrentDateView.as_view()
]