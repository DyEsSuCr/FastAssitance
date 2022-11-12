from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
  readonly_fields = ('last_login', 'date_joined', 'created_at')
  

class UserAdmin(admin.ModelAdmin):
  readonly_fields = ('last_login', 'date_joined', 'created_at')


admin.site.register(Permission)
admin.site.register(User, CustomUserAdmin)
# admin.site.register(User, UserAdmin)