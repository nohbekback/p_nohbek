from django.db import models

# Create your models here.
class Proyect(models.Model):
    names=models.CharField(max_length=150, verbose_name='Nombres')
    state=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%M/%D') #upload_to es para q se guarde el archivo x año, mes, dia
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
