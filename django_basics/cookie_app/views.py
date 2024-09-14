from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest,HttpResponse,JsonResponse

from django.views import View
from django.conf import settings

class LoginView(View):
    def get(self, request:HttpRequest):
        username = request.COOKIES.get('username')
        password = request.get_signed_cookie('password', None, salt=settings.SECRET_KEY)
        print(username, password)
        if username and password:
            return render(request, "login.html", {"username": username, "password": password})
        return render(request, "login.html")
    def post(self, request:HttpRequest):
        username = request.POST.get("username")
        password = request.POST.get("password")
        rember = request.POST.get("rember")
        print(username, password, rember)
        response = HttpResponse()
        if username == 'admin' and password == '123':
            response.content = "登陆成功"
            if rember:
                response.set_cookie('username', username)
                response.set_signed_cookie('password', password, salt=settings.SECRET_KEY, max_age=30)
            else:
                response.delete_cookie('username')
                response.delete_cookie('password')
            return response
        else:
            response.delete_cookie('username')
            response.delete_cookie('password')
            return render(request, "login.html")