from django.urls import path
from . import views
from django.views.decorators.csrf import  csrf_exempt
urlpatterns = [
    path('students/', csrf_exempt(views.StudentView.as_view()), name="students" ),
    path('students/<int:pk>/', csrf_exempt(views.StudentDetialView.as_view()), name="student_detail" ),
    path('classify/', csrf_exempt(views.ClassifyView.as_view()), name="classify"),
    path('classify/<int:pk>/', csrf_exempt(views.ClassifyDetailView.as_view()), name="classify_detail"),

    # path("api_stu/", views.students, name="api_students")

]
