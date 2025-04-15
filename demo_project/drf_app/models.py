from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100, unique=True)
    author=models.CharField(max_length=100)
    published_date=models.DateField()

class User(models.Model):
    username=models.CharField(max_length=100,unique=True)
    bio=models.TextField(max_length=500,blank=True)
