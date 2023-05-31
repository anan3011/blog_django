from django.db import models

# Create your models here.
class newpost(models.Model):
    name=models.CharField(max_length=100)
    descr=models.TextField()