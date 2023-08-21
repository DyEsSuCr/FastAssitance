from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.business.models import Business

# Create your models here.

class Profile(AbstractUser):
    # username = models.CharField('Nombre de usuario', max_length=32, unique=True)
    # email = models.CharField('Correo', max_length=50, unique=True)
    businnes = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["created_at"]
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


    # USERNAME_FIELDS = 'username'
    # REQUIRED_FIELDS = ['username', 'email']


    def __str__(self):
        return f'Usuario: {self.username}'