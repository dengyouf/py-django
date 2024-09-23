from django.shortcuts import render

# Create your views here.

# from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from apis.models import Student, Classify
from django.http import  JsonResponse
from apis.app_serializers import StudentSerializer,ClassifySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
#
# class StudentView(APIView):
#
#     def get(self,request,format=None):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         from rest_framework.response import Response
#         # return  JsonResponse({"code": 200, "data":serializer.data}, safe=False)
#         return  Response(serializer.data)
#
#     def post(self, request):
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
#
#
# class StudentDetailView(APIView):
#     def get(self,request,pid ):
#         student = Student.objects.get(pk=pid)
#         serilizer = StudentSerializer(student)
#         return JsonResponse({"code": 200, "data": serilizer.data})
#     def put(self, request, pid):
#         try:
#             student = Student.objects.get(pk=pid)
#         except Exception as e:
#             return JsonResponse({"code": 500, "data": None, "msg": "查无此用户"})
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
#     def delete(self, request, pid):
#         try:
#             student = Student.objects.get(pk=pid)
#         except Exception as e:
#             return JsonResponse({"code": 500, "data": None, "msg": "查无此用户"})
#
#         serializer = StudentSerializer(student)
#         data = JSONRenderer().render(serializer.data)
#         student.delete()
#
#         return  JsonResponse({"code": 200,"data": data.decode(encoding='utf8'),  "msg": "删除用户成功"})
#
class ClassifyView(APIView):
    def get(self,request):
        cls_list = Classify.objects.all()
        serializer = ClassifySerializer(cls_list, many=True)

        return  JsonResponse({"code": 200, "data":serializer.data}, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ClassifySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
class ClassifyDetailView(APIView):
    def get(self,request,pk ):
        cls = Classify.objects.get(pk=pk)
        serilizer = ClassifySerializer(cls)
        return JsonResponse({"code": 200, "data": serilizer.data})
    def put(self, request, pk):
        try:
            cls = Classify.objects.get(pk=pk)
        except Exception as e:
            return JsonResponse({"code": 500, "data": None, "msg": "查无此用户"})
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self, request, pid):
        try:
            cls = Classify.objects.get(pk=pid)
        except Exception as e:
            return JsonResponse({"code": 500, "data": None, "msg": "查无此用户"})

        serializer = StudentSerializer(cls)
        data = JSONRenderer().render(serializer.data)
        cls.delete()

        return  JsonResponse({"code": 200,"data": data.decode(encoding='utf8'),  "msg": "删除用户成功"})


# from rest_framework.decorators import api_view
# from rest_framework.response import  Response
# from rest_framework.request import  Request
# @api_view(["GET", "POST"])
# def students(request):
#     if request.method == 'GET':
#         stu_lst = Student.objects.all()
#         serializer = StudentSerializer(stu_lst, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


from rest_framework import mixins, generics, permissions

from apis.app_serializers import StudentSerializer, ClassifySerializer
from apis.models import Student, Classify


# class StudentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#        return  self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
#
# class StudentDetailView(mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

    # def get(self, request,  *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    # def delete(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)

class StudentView(generics.ListCreateAPIView):
    from rest_framework import permissions
    permission_classes =    [permissions.IsAuthenticatedOrReadOnly]


    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer

class StudentDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]