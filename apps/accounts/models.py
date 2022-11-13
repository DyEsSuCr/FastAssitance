from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
  class Role(models.TextChoices):
    ADMIN = 'Admin'
    EMPLOYEE = 'Employee'

  base_role = Role.ADMIN
  
  img_profile = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name='Imagen de perfil')
  created_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de creación')
  role = models.CharField(max_length=50, choices=Role.choices)

  class Meta:
    ordering = ["created_at"]
    db_table = 'auth_user'
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'


  def save(self, *args, **kwargs):
    if not self.pk:
      self.role = self.base_role
      return super().save(*args, **kwargs)


  @property
  def get_photo(self):
    if self.img_profile:
      return self.img_profile.url
    return 'https://www.fundacionmsc.cl/wp-content/uploads/2019/05/sin-imagen-2.png'


class EmployeeProfile(UserProfile):

  base_role = UserProfile.Role.EMPLOYEE

  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    proxy: True