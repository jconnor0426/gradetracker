from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, activityEdit, subactivityAdd, MyRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def whatIfView(request, course_id):
        course = get_object_or_404( Course, pk=course_id )	
        course_grade = 0
        for each in course.graded_activities_set.all()
        	course_grade = course_grade + ( each.grade_weight * each.grade_earned )
        return render(request, 'GradeTracker/whatIfPage.html', { 'course':course, 'sum': course_grade } )