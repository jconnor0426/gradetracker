# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm



#OUR PAGES!
from GradeTracker.indexView import index
from GradeTracker.auth_viewView import auth_view
from GradeTracker.logoutView import logout
from GradeTracker.accountView import account, editAccount

#Model Management Views
from GradeTracker.studentView import detail, editCourse, deleteCourse
from GradeTracker.gradedActivityView import grades, editGradedActivity, deleteGradedActivity
from GradeTracker.subGradedActivityView import addSub, deleteSubGradedActivity, editSubGradedActivity



def test(request, student_id):
    course_list = Course.objects.filter(student=student_id)
    context = {'course_list' : course_list}
    return render(request, 'GradeTracker/examples.html', context)
    
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'GradeTracker/login.html', c) 

def loggedin(request):
    student_list = Student.objects.filter(user=request.user)
    #What Happens when a student hasn't been created yet?
    #if student_list:
    return HttpResponseRedirect('/GT/' + str(student_list[0].id) + '/')
    #else:
     #   return render(request, 'GradeTracker/loggedin.html', {'full_name': request.user.username, 'student_list' : student_list})

def invalid_login(request):
    return render(request, 'GradeTracker/invalid_login.html')

'''def logout(request):
    auth.logout(request)
    return render(request, 'GradeTracker/logout.html')
'''

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #Create a new student with a link to the user
            new_student = Student( user=new_user, fName=new_user.first_name, lName=new_user.last_name, Institution=new_user.institution )  
            new_student.save()
            return HttpResponseRedirect('/GT/accounts/register_success')
    else:
        form = MyRegistrationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form        

    return render(request, 'GradeTracker/register.html', args)

def register_success(request):
    return render(request, 'GradeTracker/register_success.html')

