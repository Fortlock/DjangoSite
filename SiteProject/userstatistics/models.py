from django.db import models, transaction, IntegrityError
from django.contrib.auth.models import User
from profiles.customfields import IntegerRangeField
from django.core.exceptions import ObjectDoesNotExist
import userstatistics.simport.randomusername

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
		return str(self.year)

	

	def import_job(tasks, scores, create_users = False, abort_if_user_not_exists = True):
		#create or get users
		users = []
		for row in scores:
			names = row[0].split()
			while(len(names)<3):
					names.append(u'')
			try:
				crr_usr = User.objects.get(first_name = names[1], last_name = names[0], profile__patronymic = names[2])
				users.append(crr_usr)
			except ObjectDoesNotExist:
				users.append(None)
			#TODO if need create
		if (users.count(None)!=0 and abort_if_user_not_exists):
			return False
		#create job for job field
		db_job = Job(year = 2019)
		#create or get tasks for task field
		db_tasks = []
		for col in tasks:
			try:
				db_tasks.append(Task.objects.get(name = col))
			except ObjectDoesNotExist:
				db_tasks.append(Task(name = col))
		#create scores
		try:
			with transaction.atomic():
				for user in users:
					if (not user is None):
						user.save()
				db_job.save()
				for task in db_tasks:
					task.save()
				db_scores = []
				if (len(users) >= 2):
					for i in range(0,2):
						for j in range(1,len(row)):
							if (isinstance(scores[i][j],float) and users[i]!=None):
								my_score = int(scores[i][j])
								db_scores.append(Score(appraiser = users[i],job = db_job, task = db_tasks[j-1],score = my_score,quality = '='))
					if (len(users) == 3):
						for j in range(1,len(row)):
							if (isinstance(scores[2][j],float)):
								my_score = int(scores[2][j])
								for score in db_scores:
									if (score.task == db_tasks[j-1]):
										if (score.score < my_score):
											score.quality = '-'
										elif (score.score > my_score):
											score.quality = '+'
								if (users[2]!=None):
									db_scores.append(Score(appraiser = users[2],job = db_job, task = db_tasks[j-1],score = my_score,quality = '='))
				for score in db_scores:
					if (score.appraiser != None):
						score.save()
			return True
		except IntegrityError:
			return False

class Score(models.Model):
	appraiser = models.ForeignKey(User,on_delete=models.CASCADE)
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	task = models.ForeignKey(Task,on_delete=models.CASCADE)
	score = IntegerRangeField(min_value=0, max_value=100)
	QUALITY_CHOICES = (('+','Завысил'),('-','Занизил'),('=','Не пошла на третью проверку'))
	quality = models.CharField(max_length=1,choices=QUALITY_CHOICES)

	class Meta:
		ordering = ["score"]

	def __str__(self):
		return self.appraiser.username