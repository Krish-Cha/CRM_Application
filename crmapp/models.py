from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=5000)
    posteddate=models.CharField(max_length=30)

class customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    contactno=models.CharField(max_length=10)
    email=models.EmailField(max_length=100,primary_key=True)
    regdate=models.CharField(max_length=30)


class Valid(models.Model):
    userid=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)