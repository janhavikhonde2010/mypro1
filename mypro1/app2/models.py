from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    adress=models.CharField(max_length=100)
    salary=models.IntegerField()
    status=models.BooleanField()
