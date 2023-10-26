from django.db import models

# Create your models here.
class Proyect(models.Model):
    names=models.CharField(max_length=150, verbose_name='Nombres')
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
