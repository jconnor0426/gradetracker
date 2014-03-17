from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

def addSub(request, student_id, course_id, graded_activity_id ):
    if request.user.is_authenticated():
        student = Student.objects.filter(user=request.user)[0]
        activity = get_object_or_404( Graded_Activities, pk=graded_activity_id )
        course = get_object_or_404( Course, pk=course_id )        
        if request.method == 'POST':
            form = subactivityAdd(request.POST, instance=activity)
            if form.is_valid():
                activity.subgraded_activities_set.create( subactivity_name = form.cleaned_data['subactivityName'], subgrade_weight = form.cleaned_data['subactivityWeight'] )
                activity.save()
                form.save()
                return HttpResponseRedirect('/GT/' + str(student.id) +'/' + str(activity.course.id)  + '/' + str(activity.id) + '/')
        else:
            form = subactivityAdd()
        return render(request, 'GradeTracker/activities.html', {'form':form, 'activity':activity, 'student':student, 'course':course} )
    else: 
        return render(request, 'GradeTracker/login.html')

