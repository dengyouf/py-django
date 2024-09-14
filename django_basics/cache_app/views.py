from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest,HttpResponse
from django_redis import get_redis_connection
from django.core.cache import cache
from django.views.decorators.cache import never_cache

from django.core.cache import caches

import time

def set_func(request:HttpRequest):
    with get_redis_connection('default') as conn:
        conn.set("k1", "v1")
        conn.expire("k1", 60)  # 60s 后过期

    cache.set("foo", "bar", timeout=120) # ":1:foo"

    cache_myapp = caches['myapp']
    cache_myapp.set("k2", "v2", timeout=60)

    return HttpResponse("set success")

def get_func(request:HttpRequest):
    with get_redis_connection('default') as conn:
        value1 = conn.get("k1")
        
    value2 = cache.get("foo")

    myapp_cache = caches['myapp']
    value3 = myapp_cache.get("k2")
    return HttpResponse(f"get success {value1} -{value2}-{value3}")

def del_func(request:HttpRequest):
        with get_redis_connection('default') as conn:
            # conn.delete("k1")
            conn.flushall()
        return HttpResponse(f"delete success.")

from django.views.decorators.cache import never_cache
import datetime
# @never_cache
def global_cache(request:HttpRequest):
     t = datetime.datetime.now()
     # 如果没有开启缓存时间会变化，开启后就不会变化了
     return HttpResponse(f"Full_Cache : {t}.")

from django.views.decorators.cache import cache_page
@cache_page(5*60, cache='myapp', key_prefix="view_cache")
def view_cache(request:HttpRequest):
     t = time.time()
     # 如果没有开启缓存时间会变化，开启后就不会变化了
     return HttpResponse(f"View Cache : t:{t}")


def tmpl_cache(request:HttpRequest):
     t = time.time()
     return render(request , 'tmpl_cache.html', {"t": t})


# session cache
from django.views import View
class SessionCacheView(View):
     def get(self, request):
          username = request.session.get('username', None)
          if username:
            return render(request, 'session_cache.html', {"username": username})
          else:
               return redirect('cache_app:login') 
     
class UserView(View):
     def get(self, request):
          
          return render(request, 'sess_login.html')
     def post(self, request):
          username = request.POST.get('username')
          password = request.POST.get('password')
          if username == 'admin' and password == '123':
               request.session['username'] = username
               return redirect('cache_app:sess_cache')
          return redirect('cache_app:login')