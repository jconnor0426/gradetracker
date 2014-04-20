from django.contrib.auth.models import User
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from datetime import date, timedelta
import random


sampleClasses = [ 	("Course1", "COP101"),
			("Course2", "COP102"), 
			("Course3", "COP103"),
			("Course4", "COP104") ]

sample_activities = [ 	"Activity1",
			"Activity2",
			"Activity3" ]

sample_subactivities = [ 	"SubActivity1",
				"SubActivity2",
				"SubActivity3"]

def populate():
	#Build the list of data to populate
	first_names = [line.rstrip() for line in open('actor-givenname')]
	last_names = [line.rstrip() for line in open('actor-surname')][:len(first_names) ]

	for first, last in zip( first_names, last_names ):
		#Create the users
		new_user = User.objects.create_user( first, 'email@email.com', 'password')
		new_user.last_name = last
		new_user.institution = "FSU"
		new_user.save()
		new_student = Student( user=new_user, fName=new_user.first_name, lName=new_user.last_name, Institution=new_user.institution )  
		new_student.save()

		#Add some classes
		#loop through and create class 1, 2, 3, 4
		for course in sampleClasses:
			new_course = new_student.course_set.create( course_name = course[0] , course_code =course[1]  )
			#Add activities to each class
			#add activity 1, 2, 3, with random grades, weights, and all due Random Days in May
			for activity in sample_activities:
				new_activity = new_course.graded_activities_set.create( 	activity_name = activity , 
												grade_weight = random.random(), 
												grade_earned=random.random(),
												grade_due_date = date.today + timedelta( days=random.randint(1,50) )  )
				#for each new activity add some subactivities
				for subactivity in sample_subactivities:
					new_activity.subgraded_activities_set.create( 	activity_name = subactivity , 
											subgrade_weight = random.random(), 
											subgrade_earned=random.random(),
											subgrade_due_date = date.today + timedelta( days=random.randint(1,50) )  )
	


