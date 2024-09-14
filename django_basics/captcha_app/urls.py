from django.urls import path

from . import views

app_name = "captcha_app"

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('gen_captcha_img/', views.gen_captcha_img, name="gen_captcha_img"),
    path('logout/', views.logout, name="logout"),
]