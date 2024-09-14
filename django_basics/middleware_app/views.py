from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    print("Testing 视图函数")
    return HttpResponse('This is a test page')