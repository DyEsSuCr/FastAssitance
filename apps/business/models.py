from django.db import models
from apps.base.models import BaseModel

# Create your models here.

class Business(BaseModel):
    name = models.CharField('Nombre', max_length=60)
    address = models.CharField('Direcciom', max_length=60, unique=True)
    phone_number = models.CharField('Telefono', max_length=16, unique=True)


    class Meta:
      ordering = ["-name"]
      verbose_name = 'Negocio'
      verbose_name_plural = 'Negocios'


    def __str__(self):
      return f'{self.name}'