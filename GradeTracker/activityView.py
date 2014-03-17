from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

def addSub(request, student_id, course_id, activity_id ):
    if request.user.is_authenticated():
        student = Student.objects.filter(user=request.user)[0]
        activity = get_object_or_404( Graded_Activities, pk=activity_id )
        
        if request.method == 'POST':
            form = subactivityAdd(request.POST, instance=activity)
            if form.is_valid():
                form.save()

            return HttpResponseRedirect('/GT/' + str(student.id) +'/' + str(activity.course.id)  + '/' + str(activity.id) + '/')
        return render(request, 'GradeTracker/activities.html')
    else: 
        return render(request, 'GradeTracker/login.html')

