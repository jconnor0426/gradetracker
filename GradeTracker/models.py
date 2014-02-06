from django.db import models

# Create your models here.
class Student(models.Model):
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
