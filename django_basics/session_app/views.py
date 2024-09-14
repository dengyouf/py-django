from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def set_session(reqeust:HttpRequest):
    reqeust.session['uname'] = "admin"
    reqeust.session['email'] = "admin@example.com"

    return HttpResponse("Session set successfully")

def get_session(reqeust:HttpRequest):
    uname = reqeust.session.get('uname')
    email = reqeust.session.get('email')

    time = reqeust.session.get_expiry_age()
    date = reqeust.session.get_expiry_date()
    return HttpResponse(f"Session get successfully {uname} {email} <br/> {date}<br/>{time}")

def del_session(reqeust:HttpRequest):
    # reqeust.session.flush()
    reqeust.session.clear()

    return HttpResponse("Session deleted successfully")




# @login_required(login_url="/session_app/login/")
@login_required(login_url="session_app:login")
def index(reqeust:HttpRequest):
    
    return render(reqeust, "indexs.html")

class LoginView(View):

    def get(self, reqeust:HttpRequest):
       print(reverse('session_app:login'))
       return render(reqeust, "logins.html", {"error_msg": None})
    
    def post(self, request:HttpRequest):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)  # 登陆成功后，将user添加到request.user中
            request.session['uname'] = username
            request.session['email'] = user.email
            return redirect('session_app:index')
        else:
            return render(request, "logins.html", {"error_msg": "Invalid username or password"})
    
def logout(reqeust:HttpRequest):
    del reqeust.session['uname']
    del reqeust.session['email']
    auth.logout(reqeust)  # 登出成功后，将user从request.user中删除
    return redirect('session_app:login')