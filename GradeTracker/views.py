# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, MyRegistrationForm

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST': # If the form has been submitted...
        form = courseAdd(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            student.course_set.create( course_name = form.cleaned_data['courseName'], course_code = form.cleaned_data['courseCode'] )            
            return HttpResponseRedirect('/GT/' + str(student_id) ) # Redirect after POST
    else:
        form = courseAdd() # An unbound form
    return render(request, 'GradeTracker/detail.html', {'student': student , 'form': form })

def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list }
    return render( request, 'GradeTracker/index.html', context )  

def grades(request, student_id, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST': # If the form has been submitted...
        form = activityAdd(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            course.graded_activities_set.create( activity_name = form.cleaned_data['activityName'], grade_weight = form.cleaned_data['activityWeight'] )
            return HttpResponseRedirect('/GT/' + str(student_id) + "/" + str(course_id)) # Redirect after POST
    else:
        form = activityAdd()
    return render(request, 'GradeTracker/grades.html', {'course': course , 'student': course.student , 'form': form })

def main(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list }
    return render (request, 'GradeTracker/main.html', context)

def deleteCourse( request, course_id ):
    course = get_object_or_404( Course, pk=course_id )
    studentReturned = course.student.id
    course.delete()
    return HttpResponseRedirect( '/GT/' + str(studentReturned ) )

def test(request, student_id):
    course_list = Course.objects.filter(student=student_id)
    context = {'course_list' : course_list}
    return render(request, 'GradeTracker/examples.html', context)
    
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'GradeTracker/login.html', c) 

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

def loggedin(request):
    return render(request, 'GradeTracker/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render(request, 'GradeTracker/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'GradeTracker/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/GT/accounts/register_success')
    else:
        form = MyRegistrationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form        

    return render(request, 'GradeTracker/register.html', args)

def register_success(request):
    return render(request, 'GradeTracker/register_success.html')
