from django.urls import path
from . import views
app_name = "cache_app"
urlpatterns =[
    path("set/", views.set_func, name="set"),
    path("get/", views.get_func, name="get"),
    path("del/", views.del_func, name="del"),
    path("global_cache/", views.global_cache, name="global_cache"),
    path("view_cache/", views.view_cache, name="view_cache"),
    path("tmpl_cache/", views.tmpl_cache, name="tmpl_cache"),
    path("sess_login/", views.UserView.as_view(), name="login"),
    path("sess_cache/", views.SessionCacheView.as_view(), name="sess_cache"),
]