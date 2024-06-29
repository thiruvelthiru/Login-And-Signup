from django.db import models

# Create your models here.
class Datas(models.Model):
    name = models.CharField(max_length=20,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=20,default="")
    confirm_password = models.CharField(max_length=20,default="")

    