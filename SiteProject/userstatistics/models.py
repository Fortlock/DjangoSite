from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from profiles.customfields import IntegerRangeField

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=20, help_text="Введите название задачи", unique = True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Job(models.Model):
	year = IntegerRangeField(min_value=2000, max_value=2100)

	class Meta:
		ordering = ["year"]

	def __str__(self):
		return self.appraiser.username

class Score(models.Model):
	appraiser = models.ForeignKey(User,on_delete=models.CASCADE)
	task = models.ForeignKey(Task,on_delete=models.CASCADE)
	score = IntegerRangeField(min_value=0, max_value=100)
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	QUALITY_CHOICES = (('+','Завысил'),('-','Занизил'),('=','Не пошла на третью проверку'))
	quality = models.CharField(max_length=1,choices=QUALITY_CHOICES)

	class Meta:
		ordering = ["score"]

	def __str__(self):
		return self.appraiser.username