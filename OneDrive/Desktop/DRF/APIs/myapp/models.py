from django.db import models
from django.core.paginator import EmptyPage

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']