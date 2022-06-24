from datetime import datetime
from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length= 30)
    edad =  models.IntegerField()
    # dt = datetime.now()
    # fecha_creacion = models.DateField({dt})
    fecha_creacion = models.DateField(null=True)
    