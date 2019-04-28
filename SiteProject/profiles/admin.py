from django.contrib import admin

# Register your models here.

from .models import Category, Profile

admin.site.register(Category)
admin.site.register(Profile)