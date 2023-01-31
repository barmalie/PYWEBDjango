from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

class LoginView(View):
    def get(self, request):
       return render(request, 'login/index_login_2.html')

    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})
