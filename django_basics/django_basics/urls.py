"""django_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookie_app/', include("cookie_app.urls")),
    path('session_app/', include("session_app.urls")),
    path('paging_app/', include("paging_app.urls")),
    path('captcha_app/', include("captcha_app.urls")),
    path('middleware_app/', include("middleware_app.urls")),
    path('logging_app/', include("logging_app.urls")),
    path('cache_app/', include("cache_app.urls")),
]
