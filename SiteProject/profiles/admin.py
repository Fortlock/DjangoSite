from django.contrib import admin

# Register your models here.

from .models import Category, Profile, Education, Post, AcademicDegree

admin.site.register(Category)
admin.site.register(Education)
admin.site.register(Post)
admin.site.register(AcademicDegree)
admin.site.register(Profile)