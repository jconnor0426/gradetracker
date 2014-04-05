# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm



#OUR PAGES!
from GradeTracker.welcomeView import welcome
from GradeTracker.indexView import index
from GradeTracker.auth_viewView import auth_view
from GradeTracker.logoutView import logout
from GradeTracker.accountView import account, editAccount

#Model Management Views
from GradeTracker.studentView import detail, editCourse, deleteCourse
from GradeTracker.gradedActivityView import grades, editGradedActivity, deleteGradedActivity
from GradeTracker.subGradedActivityView import addSub, deleteSubGradedActivity, editSubGradedActivity

#User Features Page
from GradeTracker.whatIfView import whatIfView

#Template Search Engine 
from GradeTracker.courseTemplatesView import searchTemplateView#, addTemplateView
#from GradeTracker.testServices import googleTest



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

def googleTest(request):
    import mainproc
    import requests
    import json
    import time
    import subprocess
    from oauth2 import OAuthDeviceFlow

    CODE_URI = 'https://accounts.google.com/o/oauth2/device/code'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    CLIENT_ID='453267463678-0mesdcmqj8b3m4lmc3ahv7losu7f1fe7.apps.googleusercontent.com'
    CLIENT_SECRET='1RTctpITEaTLF9fGV5ZifQH1'
    SCOPE='https://www.googleapis.com/auth/calendar.readonly'

    oauth = OAuthDeviceFlow(
        code_uri=CODE_URI,              # URI for obtaining OAuth user code
        token_uri=TOKEN_URI,            # URI for obtaining OAuth tokens
        client_id=CLIENT_ID,            # OAuth Client ID
        client_secret=CLIENT_SECRET,    #
        scope=SCOPE
    )

    oauth.authorize()
    argumentstring = str(CODE_URI)+" "+str(TOKEN_URI)+" "+str(CLIENT_ID)+" "+str(CLIENT_SECRET)+" "+str(SCOPE)+" "+str(oauth._access_token)+" "+str(oauth._token_type)+" "+str(oauth._expires)+" "+str(oauth._refresh_token)+" "+str(oauth._device_code)+" "+str(oauth._expires_in)+" "+str(oauth._interval)
    subprocess.Popen(["nohup","python","/home/jconnor/GradeTracker/gradetracker/GradeTracker/spawnedproc.py",argumentstring])
    print("done")

    user = User.objects.get(id=request.user.id)
    current_student = Student.objects.filter(user=request.user)[0]
    courses = Courses.objects.filter(student=current_student.id)
    
    google = {'oauth':oauth._user_code}
        
    return render(request, "GradeTracker/calendar.html", google) 
