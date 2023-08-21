from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from apps.business.models import Business
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', max_length=32, unique=True)
    email = models.CharField('Correo', max_length=50, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    businnes = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        ordering = ["created_at"]
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()


    def __str__(self):
        return f'Usuario: {self.email}'