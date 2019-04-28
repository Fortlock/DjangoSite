from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from profiles.customfields import IntegerRangeField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=20, help_text="Р’РІРµРґРёС‚Рµ РЅР°Р·РІР°РЅРёРµ РєР°С‚РµРіРѕСЂРёРё")

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
	patronymic = models.CharField(max_length=200, help_text='Р’РІРµРґРёС‚Рµ РѕС‚С‡РµСЃС‚РІРѕ', null=True)
	pasport_series = models.CharField(max_length=4, validators=[RegexValidator(regex=r'\d{4}')], null=True)
	pasport_number = models.CharField(max_length=6, validators=[RegexValidator(regex=r'\d{6}')], null=True)
	year_of_birth = IntegerRangeField(min_value=1900, max_value=2050, null=True)
	category = models.ForeignKey(Category,on_delete=models.PROTECT, null=True)
	
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
