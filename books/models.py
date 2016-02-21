from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Books(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pb_date = models.DateTimeField("Date Published",auto_now_add = True)
	description = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username