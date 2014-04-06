from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates


def calculateClassGrade( course ):
	#make sure each activity has an up to date grade earned
	for activity in course.graded_activities_set.all():
		#If there are sub activities calculate that activities value, and save it in grade_earned
		if activity.subgraded_activities_set.all():
			activityGradeFromSubActivities( activity )
  
	#Go Through all the activities just add weight times grade earned
	#Set a total, to be zero
	classGrade = 0
	#Go through all the activities
	for activity in course.graded_activities_set.all():
		classGrade += activity.grade_weight * activity.grade_earned
	return classGrade

def activityGradeFromSubActivities( activity ):
	activitygrade = 0
	for each in activity.subgraded_activities_set.all():
		activitygrade += each.subgrade_weight * each.subgrade_earned
		activity.grade_earned = activitygrade
	activity.save()     
