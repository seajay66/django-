from django.db import models

# Create your models here.
class Classes(models.Model):
    """
    班级表
    """
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teacher")

class Teacher(models.Model):
    """
    老师表
    """
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)

# class C2T(models.Model):
#     cid = models.ForeignKey(Classes)
#     tid = models.ForeignKey(Teacher)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    addr = models.CharField(max_length=32)
    gender = models.BooleanField()
    cs = models.ForeignKey("Classes",on_delete=models.CASCADE,)
