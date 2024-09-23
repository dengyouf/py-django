from rest_framework import serializers
from  apis.models import * 

'''
$ python manage.py  shelld
>>> from apis.app_serializers import StudentSerializer 
>>> stu_ser = StudentSerializer()                                 
>>> print(repr(stu_ser)) 
StudentSerializer():
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=20)
    age = IntegerField(allow_null=True, max_value=9223372036854775807, min_value=-9223372036854775808, required=False)
    sex = ChoiceField(choices=[(0, '女'), (1, '男')], required=False, validators=[<django.core.validators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
>>> from  apis.models import * 
>>> stu =Student.objects.get(pk=1)
>>> stu_ser = StudentSerializer(stu)
>>> stu_ser.data
{'id': 1, 'name': '小红', 'age': 23, 'sex': 1}
>>> from rest_framework.renderers import JSONRenderer
>>> data_json = JSONRenderer().render(stu_ser.data)
>>> data_json
b'{"id":1,"name":"\xe5\xb0\x8f\xe7\xba\xa2","age":23,"sex":1}'

>>> stus =Student.objects.all()   
>>> stus
<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>
>>> stus_ser = StudentSerializer(stus, many=True) 
>>> stus_ser.data
[{'id': 1, 'name': '小红', 'age': 23, 'sex': 1}, {'id': 2, 'name': '小强', 'age': 24, 'sex': 0}]
>>> JSONRenderer().render(stus_ser.data)         
b'[{"id":1,"name":"\xe5\xb0\x8f\xe7\xba\xa2","age":23,"sex":1},{"id":2,"name":"\xe5\xb0\x8f\xe5\xbc\xba","age":24,"sex":0}]'
'''

class ClassRelateField(serializers.RelatedField):
    def to_representation(self, value):
        return {"id": value.id, "name": value.name}

class StudentSerializer(serializers.ModelSerializer):

    # classify = ClassifySerializer()
    classify = ClassRelateField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 'classify']
        # fields = '__all__'

class ClassifySerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Classify
        fields = ['id', 'name', 'students']