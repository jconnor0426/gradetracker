from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

def index(request):
    if request.user.is_authenticated():
        student_list = Student.objects.all()
        context = {'student_list': student_list }
        return render (request, 'GradeTracker/index.html', context)
    else: 
        return render(request, 'GradeTracker/login.html')
