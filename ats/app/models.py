from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    date_of_join = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Teacher(models.Model):
    age=models.IntegerField(null=True)
    phnoenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=20)    
    images=models.ImageField(upload_to='image/',null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
