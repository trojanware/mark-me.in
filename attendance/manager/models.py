from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.OneToOneField(User)	
	college = models.CharField(max_length=255)
	branch = models.CharField(max_length=255)
	sememster = models.CharField(max_length=255)
	section = models.CharField(max_length=255,default="")
	usn = models.CharField(max_length=255,default="")
	
	def create_user_profile(sender,instance,created,**kwargs):
		if created:	
			UserProfile.objects.create(user=instance)
	post_save.connect(create_user_profile,sender=User)

class tbl_Temp_Signup(models.Model):
	username = models.CharField(max_length=255)
	passwrd = models.CharField(max_length=255)
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	timestamp = models.DateTimeField(True,True)

class Subject(models.Model):
	user = models.ForeignKey(User)
	name=models.CharField(max_length=255)
	totaldays = models.IntegerField(default=0)
	present = models.IntegerField(default=0)
	absent = models.IntegerField(default=0)
	percentage = models.DecimalField(max_digits=8,decimal_places=2,default=0)	
	
	def __unicode__(self):
		return self.name
	def getNoPresent(self):
		return self.present
	def getTotal(self):
		return self.totaldays
	def getAbsent(self):
		return self.absent
	def getPer(self):
		return self.percentage

class Timetable(models.Model):
	subject = models.ForeignKey(Subject)
	user = models.ForeignKey(User)
	mon = models.CharField(max_length=7)
	tue = models.CharField(max_length=7)
	wed = models.CharField(max_length=7)
	thu = models.CharField(max_length=7)
	fri = models.CharField(max_length=7)
	sat = models.CharField(max_length=7)
	sun = models.CharField(max_length=7)
