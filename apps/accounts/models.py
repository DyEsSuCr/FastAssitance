from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  img_profile = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name='Imagen de perfil', help_text='Tamaño maximo de imagen 400*400')
  created_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de creación')
  is_admin = models.BooleanField(default=False)
  
  class Meta:
    ordering = ["created_at"]
    db_table = 'auth_user'

  @property
  def get_photo(self):
    if self.img_profile:
      return self.img_profile.url
    return 'https://www.fundacionmsc.cl/wp-content/uploads/2019/05/sin-imagen-2.png'

  @property
  def full_name(self):
    if self.first_name and self.last_name:
      return f'{self.first_name} {self.last_name}'
    return self.username


""" class Customer(models.Model):
  firt_name = models.CharField(max_lenght=150)
  last_name = models.CharField(max_lenght=150)
  email = models.EmailField(max_lenght=150)
  document = models.CharField(max_lenght=150)
  employee = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'customer'


  def __str__(self):
    return f'{self.firt_name - self.last_name - self.document}' """