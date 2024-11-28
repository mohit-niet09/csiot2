from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField()
    emp_id = models.CharField(max_length=10)
