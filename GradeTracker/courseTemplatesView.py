from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm, templateSearch


@login_required
def searchTemplateView( request ):
	results = []
	if request.method == 'POST': # If the form has been submitted...
		form = templateSearch(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			searchCode =  form.cleaned_data['courseCode']
			results = Course.objects.filter( course_code=searchCode )
			form = templateSearch()
			return render(request, 'GradeTracker/searchTemplates.html', {'results': results  , 'form': form , 'results_page':"yes" })
	else:
		form = templateSearch()
		return render(request, 'GradeTracker/searchTemplates.html', {'results': results  , 'form': form })

@login_required
def addTemplateView( request, course_id ):
	#Get object to copy
	courseToCopy = get_object_or_404(Course, pk=course_id )
	student = Student.objects.filter( user=request.user )[0]
	#Create a new Course Object for the current user
	newCourse = student.course_set.create( course_id=courseToCopy.id, course_name=courseToCopy.course_name )
	#Create each activity in the course object
	return HttpResponseRedirect('/GT/' + str(student.id) ) # Redirect after POST

