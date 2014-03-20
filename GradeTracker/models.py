from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User)
	fName = models.CharField( max_length=200 )
	lName = models.CharField( max_length=200 )
	Institution = models.CharField( max_length=200 )
	def __str__(self):
		return self.fName + ' ' + self.lName

class Course(models.Model):
	student = models.ForeignKey('Student')
	course_name  = models.CharField(max_length=200)
	course_code  = models.CharField(max_length=200)
	def __str__(self):
		return   self.student.fName + '-' + self.course_name

class Graded_Activities(models.Model):
	course = models.ForeignKey('Course')
	activity_name = models.CharField(max_length=200)
	#set grade_weight minimum and maximum from 0-100% represented as 0-1
	grade_weight = models.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(1.00)])
	grade_earned = models.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(1.00)], null=True)
	grade_due_date = models.DateField(null=True)
	def __str__(self):
		return self.course.student.fName + '-' + self.activity_name + ':' + str(self.grade_weight)

class SubGraded_Activities(models.Model):
	main_category = models.ForeignKey('Graded_Activities')
	subactivity_name = models.CharField(max_length=200)
	subgrade_weight = models.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(1.00)])
	subgrade_earned = models.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(1.00)], null=True)
	subgrade_due_date = models.DateField(null=True)
	def __str__(self):
		return (self.main_category.activity_name + ':' +  str(self.main_category.grade_weight) + 
		'     ' + self.subactivity_name + ':' + str(self.subgrade_weight))

class Templates(models.Model):
	course = models.ForeignKey('Course')
	institution = models.CharField(max_length=200)
	def __str__(self):
		return (self.course.course_name + " : " + self.institution)
