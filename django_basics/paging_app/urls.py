from django.urls import path

from . import views

urlpatterns = [
    path('student_all/', views.studentView.as_view()),
    path('student_page_list/', views.studentPageView.as_view()),
]