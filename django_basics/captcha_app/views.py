from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from io import BytesIO

# @login_required(login_url="captcha_app:login")
def index(requst):
    return render(requst, "indexc.html")

class LoginView(View):
    def get(self, request):
        return render(request, "loginc.html")
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_code = request.POST.get('check_code').lower()
        print('++++',check_code, request.session.get('check_code'))
        if check_code == request.session.get('check_code').lower():
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('captcha_app:index')
            else:
                return render(request, "loginc.html", {"username": username, 'msg': "Invalid username or password."})
        else:
            return render(request, "loginc.html", {"username": username, 'msg': "验证码错误."})
        
def logout(request):
    auth.logout(request)
    return redirect('captcha_app:login')

def gen_captcha_img(request):
    from .utils import captcha
    stream = BytesIO()
    img, code = captcha.veri_code()
    print(code)
    img.save(stream, 'PNG')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())