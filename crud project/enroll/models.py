from django.db import models

# Create your models here.
class kashif(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
