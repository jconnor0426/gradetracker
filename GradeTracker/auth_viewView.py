from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    #says user exists
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        #signifies user is logged in
        auth.login(request, user)
        return HttpResponseRedirect('/GT/accounts/loggedin')
    else:
        return HttpResponseRedirect('/GT/accounts/invalid')

