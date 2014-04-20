from django.contrib.auth.models import User
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates


def populate():
	#Build the list of data to populate
	first_names = [line.rstrip() for line in open('actor-givenname')]
	last_names = [line.rstrip() for line in open('actor-surname')][:len(first_names) ]

	for a,b in zip( first_names, last_names ):
		print a + '\t' + b

"""
	#For each in the list do this:
	for each in first_names:

		#Create the users
		user = User.objects.create_user(, 'lennon@thebeatles.com', 'johnpassword')
		user.last_name = 'Lennon'
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name =
		user.institution =
		user.save()

		new_student = Student( user=new_user, fName=new_user.first_name, lName=new_user.last_name, Institution=new_user.institution )  
		new_student.save()

		#Add some classes
		#loop through and create class 1, 2, 3, 4
		new_student.course_set.create( course_name = course_to_save.course_name , course_code =course_to_save.course_code  )

		#Add activities to each class
		for course in new_student.course_set.all():
			#add activity 1, 2, 3, with random grades, weights, and all due Random Days in May
			for activity in sample_activities:
				new_activity = course.graded_activities_set.create( activity_name = form.cleaned_data['activityName'], grade_weight = form.cleaned_data['activityWeight'], grade_earned=form.cleaned_data['activity_Grade_Earned'] )
				#for each new activity add some subactivities
				for subactivity in sample_subactivities:
					new_activity.subgraded_activities_set.create(activity_name = form.cleaned_data['activityName'], grade_weight = form.cleaned_data['activityWeight'], grade_earned=form.cleaned_data['activity_Grade_Earned']  )
	"""


