from django.contrib import admin
from .models import Business

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')

admin.site.register(Business, BusinessAdmin)