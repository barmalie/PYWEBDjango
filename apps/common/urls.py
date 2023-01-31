'''
   Django проект не знает о существовании файла urls.py из приложения common,
поэтому необходимо включить все маршруты приложения common в файл urls.py проекта.
Сделать это можно с помощью команды include.
'''

from django.urls import path

from .views import CurrentDateView, IndexView

urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()), # создается маршрут, который связывает url datetime/ и представление  CurrentDateView.as_view()
]