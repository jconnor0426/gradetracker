from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import User, Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import userEdit, studentEdit, courseAdd, activityAdd, subactivityAdd, MyRegistrationForm

def account(request, student_id):
    user = User.objects.filter(id=request.user.id)
    student= Student.objects.get(id=student_id)
    return render (request, 'GradeTracker/accountInfo.html', {'user':user, 'student':student})

def editAccount(request, student_id):
    student = Student.objects.get(id=student_id)
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = userEdit(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/GT/' + str(student_id) + '/account')
    else:
        form = userEdit(instance=user)
    return render(request, 'GradeTracker/account.html', {'form':form, 'user':user, 'student':student} )
