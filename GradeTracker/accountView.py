from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import User, Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import userEdit, studentEdit, courseAdd, activityAdd, subactivityAdd, MyRegistrationForm, passwordForm

def account(request, student_id):
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(id=student_id)
    return render (request, 'GradeTracker/accountInfo.html', {'user':user, 'student':student})

def editAccount(request, student_id):
    student = Student.objects.get(id=student_id)
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        passForm = passwordForm( request.POST )
        userForm = userEdit(request.POST, instance=user)
        studentForm = studentEdit(request.POST, instance=student)
        if userForm.is_valid() and studentForm.is_valid() and passForm.is_valid():
            print user
            print passForm.cleaned_data['password' ]
            user.set_password( passForm.cleaned_data['password']  ) 
            userForm.save()
            studentForm.save()
            user.save()
            return HttpResponseRedirect('/GT/' + str(student_id) + '/account')
    else:
        userForm = userEdit(instance=user)
        studentForm = studentEdit(instance=student)
        passForm = passwordForm()
    return render(request, 'GradeTracker/account.html', {'passForm':passForm, 'userForm':userForm, 'studentForm':studentForm, 'user':user, 'student':student} )
