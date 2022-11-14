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
  ADMIN = 'AD'
  EMPLOYEE = 'EM'

  ROLE = [
    (ADMIN, 'Administrador'),
    (EMPLOYEE, 'Empleado')
  ]

  base_role = ADMIN
  
  img_profile = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name='Imagen de perfil')
  created_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de creación')
  role = models.CharField(max_length=50, choices=ROLE, verbose_name='Rol')
  business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Negocio')

  class Meta:
    ordering = ["created_at"]
    db_table = 'auth_user'
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'


  def save(self, *args, **kwargs):
    if not self.pk:
      self.role = self.base_role
      return super().save(*args, **kwargs)
    return super().save(*args, **kwargs)


  @property
  def get_photo(self):
    if self.img_profile:
      return self.img_profile.url
    return 'https://www.fundacionmsc.cl/wp-content/uploads/2019/05/sin-imagen-2.png'
  

class AdminProfile(UserProfile):

  base_role = UserProfile.ADMIN

  class Meta:
    verbose_name = 'Administrador'
    verbose_name_plural = 'Administradores'
    proxy: True


class EmployeeProfile(UserProfile):

  user = models.ForeignKey(AdminProfile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado por')
  base_role = UserProfile.EMPLOYEE

  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    proxy: True