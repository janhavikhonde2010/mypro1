from django.db import models

# Create your models here.
from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email_id = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
