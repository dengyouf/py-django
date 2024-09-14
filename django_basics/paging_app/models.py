from django.db import models
from string import  ascii_lowercase,digits
# Create your models here.
import random

class Student(models.Model):
    class Meta:
        db_table = 't_student'
        verbose_name_plural = "学生表"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField(choices=((0, "女"),(1, "男")), default=0)
    card_no = models.CharField(max_length=18)


    @classmethod
    def insert_test_data(cls, num=100):
        def random_str(raw_item, length):
            return ''.join(random.choices(raw_item, k=length))
        
        obj_list = []
        for _ in range(num):
            obj_list.append(Student(
                name=random_str(ascii_lowercase, 6),
                age=random.randint(18, 45),
                sex=random.choice([0, 1]),
                card_no=random_str(digits, 18),
            ))

        Student.objects.bulk_create(obj_list)


# $ python manage.py  shell
# >>> from paging_app.models import Student
# >>> Student.insert_test_data(num=4)