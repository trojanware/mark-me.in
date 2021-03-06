from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class timetable(models.Model):
	subject_user_rel = models.IntegerField()
	mon = models.IntegerField()
	tue = models.IntegerField()
	wed = models.IntegerField()
	thu = models.IntegerField()
	fri = models.IntegerField()
	sat = models.IntegerField()
	sun = models.IntegerField()

class Subjects(models.Model):
	subj_id = models.IntegerField(primary_key=True)
	Subject = models.CharField(max_length=50)

class Users(models.Model):
	user_id = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=50)

class tbl_user_subject_rel(models.Model):
	user_subject_id = models.IntegerField(primary_key=True)
	user_id = models.IntegerField()
	subject_id = models.IntegerField()

class TotalWorkingDays(models.Model):
	user_subject_rel = models.ForeignKey(tbl_user_subject_rel,primary_key=True)
	totalworkingdays = models.IntegerField()

class PresentDates(models.Model):
	user_subject_rel = models.ForeignKey(tbl_user_subject_rel,primary_key=True)
	present = models.IntegerField()

class AbsentDates(models.Model):
	user_subject_rel = models.ForeignKey(tbl_user_subject_rel,primary_key=True)
	absent = models.IntegerField()

class tbl_user_subject_rel(models.Model):
	user_subject_id = models.AutoField(primary_key=True)
	user_id = models.IntegerField()
	subject_id = models.IntegerField()
class tbl_Temp_Signup(models.Model):
	username = models.CharField(max_length=255)
	passwrd = models.CharField(max_length=255)
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
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
	
