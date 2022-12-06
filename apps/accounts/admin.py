from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import Business, UserProfile

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'phone_number', 'img_business')
  list_editable = ('img_business',)


class ProfileAdmin(UserAdmin):
  list_display = ('username', 'role', 'img_profile', 'business')
  list_editable = ('role', 'img_profile', 'business')
  ordering = ['role']


admin.site.register(Permission)
admin.site.register(Business, BusinessAdmin)
admin.site.register(UserProfile, ProfileAdmin)