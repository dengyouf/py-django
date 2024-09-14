from django.urls import path
from . import views

app_name = "session_app"
urlpatterns = [
    path("set/",  views.set_session),
    path("get/",  views.get_session),
    path("del/",  views.del_session),

    # 使用案例
    path("", views.index, name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
]