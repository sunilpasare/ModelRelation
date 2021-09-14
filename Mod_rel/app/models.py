from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import widgets

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=20)
    dintake=models.IntegerField()
    
    def __str__(self):
        return self.dname


class Student(models.Model):
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    rn=models.IntegerField()
    sname=models.CharField(max_length=20)
    marks=models.FloatField()

    def __str__(self):
        return self.sname

class Lecture(models.Model):
    Department=models.ManyToManyField(Department)
    sal=models.FloatField()
    lname=models.CharField(max_length=20)

    def __str__(self):
        return self.lname


