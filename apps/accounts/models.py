from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Business(models.Model):
  name = models.CharField('Nombre', max_length=60)
  address = models.CharField('Direccion', max_length=50)
  phone_number = models.CharField('Telefono', max_length=12)
  img_business = models.ImageField('Imagen del negocio', upload_to='business', blank=True, null=True)

  class Meta:
    ordering = ["-name"]
    verbose_name = 'Negocio'
    verbose_name_plural = 'Negocios'
    

  def __str__(self):
    return f'{self.name}'


  @property
  def get_photo(self):
    if self.img_business:
      return self.img_business.url
    return 'https://www.mifoto.cl/wp-content/uploads/2022/01/sin-imagen.jpg'


class UserProfile(AbstractUser):
  ADMIN = 'ADMIN'
  EMPLOYEE = 'EMPLOYEE'

  ROLE = [
    (ADMIN, 'Administrador'),
    (EMPLOYEE, 'Empleado')
  ]
  
  img_profile = models.ImageField('Imagen de perfil', upload_to='photo', blank=True, null=True)
  created_at = models.DateTimeField('Fecha de creación', auto_now=True, auto_now_add=False)
  role = models.CharField('Rol', max_length=50, choices=ROLE)
  business = models.ForeignKey(Business, on_delete=models.CASCADE, default=EMPLOYEE, null=True, blank=True)

  class Meta:
    ordering = ["created_at"]
    db_table = 'auth_user'
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'


  @property
  def get_photo(self):
    if self.img_profile:
      return self.img_profile.url
    return 'https://www.fundacionmsc.cl/wp-content/uploads/2019/05/sin-imagen-2.png'