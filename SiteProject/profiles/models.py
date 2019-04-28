from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from profiles.customfields import IntegerRangeField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=20, help_text="Введите название категории")

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Education(models.Model):
	name = models.CharField(max_length=20, help_text = 'Введите образование')

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Post(models.Model):
	name = models.CharField(max_length=20, help_text = 'Введите образование')

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class AcademicDegree(models.Model):
	name = models.CharField(max_length=20, help_text = 'Введите образование')

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
	patronymic = models.CharField(max_length=200, help_text='Введите отчество', null=True)
	pasport_series = models.CharField(max_length=4, validators=[RegexValidator(regex=r'\d{4}')], null=True)
	pasport_number = models.CharField(max_length=6, validators=[RegexValidator(regex=r'\d{6}')], null=True)
	year_of_birth = IntegerRangeField(min_value=1900, max_value=2050, null=True)
	job_if_education = models.CharField(max_length=200, help_text='Введите образовательное учреждение', null=True)
	job_if_not_education = models.CharField(max_length=200, help_text='Введите место работы', null=True)
	education = models.ForeignKey(Education,on_delete=models.PROTECT, null=True)
	category = models.ForeignKey(Category,on_delete=models.PROTECT, null=True)
	qualification = models.CharField(max_length=200, help_text='Введите квалификацию(по диплому)',null=True)
	post = models.ForeignKey(Post,on_delete=models.PROTECT,null=True)
	academic_degree = models.ForeignKey(AcademicDegree,on_delete=models.PROTECT,null=True)
	work_experience = IntegerRangeField(min_value=0, max_value=120, null=True)
	YES_NO_CHOICES = (('да','да'),('нет','нет'))
	third_check = models.CharField(max_length=3,choices=YES_NO_CHOICES,null=True)
	conflict = models.CharField(max_length=3, choices=YES_NO_CHOICES,null=True)

	class Meta:
		ordering = ['year_of_birth']

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
