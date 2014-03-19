from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

@login_required
def addSub(request, student_id, course_id, graded_activity_id ):
    if request.user.is_authenticated():
        student = Student.objects.filter(user=request.user)[0]
        activity = get_object_or_404( Graded_Activities, pk=graded_activity_id )
        course = get_object_or_404( Course, pk=course_id )        
        if request.method == 'POST':
            form = subactivityAdd(request.POST)
            if form.is_valid():
                activity.subgraded_activities_set.create( subactivity_name = form.cleaned_data['subactivityName'], subgrade_weight = form.cleaned_data['subactivityWeight'] )
                return HttpResponseRedirect('/GT/' + str(student.id) +'/' + str(activity.course.id)  + '/' + str(activity.id))
        else:
            form = subactivityAdd()
        return render(request, 'GradeTracker/activities.html', {'form':form, 'activity':activity, 'student':student, 'course':course} )
    else: 
        return render(request, 'GradeTracker/login.html')

@login_required
def deleteSubGradedActivity(request, subactivity_id):
    student = Student.objects.filter(user=request.user)[0]
    subactivity = get_object_or_404(SubGraded_Activities, pk=subactivity_id)
    activityReturned = subactivity.main_category.id
    courseReturned = activityReturned.course
    subactivity.delete()
    return HttpResponseRedirect('/GT/' + str(courseReturned.student.id) +'/' + str(courseReturned.id)  + '/'  + str(activityReturned) + '/' )

@login_required
def editSubGradedActivity(request, subactivity_id):
    subactivity = get_object_or_404( SubGraded_Activities, pk=subactivity_id ) #Get the Graded_Activity to edit
    activity= subactivity.main_category
    courseReturned = 

    student = Student.objects.filter(user=request.user)[0]

    if request.method == 'POST':            # If the form has been submitted...
        form = subactivityEdit(request.POST, instance=subactivity) # A form bound to the POST data, with the activity loaded
        if form.is_valid():                 # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()

            return HttpResponseRedirect('/GT/' + str(student.id) +'/' + str(courseReturned.id)  + '/' + ) # Redirect after POST
    else:
        form = activityEdit(instance=activity) # An unbound form
    return render(request, 'GradeTracker/editActivity.html', { 'form': form , 'activity':activity} )
