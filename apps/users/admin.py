from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.

class ProfileAdmin(UserAdmin):
    list_display = ('username', 'created_at')

admin.site.register(Profile, ProfileAdmin)
