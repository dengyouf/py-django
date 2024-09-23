from django.db import models

# Create your models here.
class Classify(models.Model):
    name = models.CharField(max_length=20)
class Student(models.Model):
    SEX_CHOICES = ((0, '女'),(1, '男'))
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(choices=SEX_CHOICES, default=1)

    classify = models.ForeignKey(Classify, related_name="students", on_delete=models.SET_NULL, null=True)

