from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField(unique=True)
    marks=models.FloatField()
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    address=models.TextField(null=True)

    trainer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name