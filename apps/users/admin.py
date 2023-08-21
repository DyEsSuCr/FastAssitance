from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')


admin.site.register(User, CustomUserAdmin)
 