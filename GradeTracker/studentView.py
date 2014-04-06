from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm
from GradeTracker.utilities import calculateClassGrade

## Page that shows the student overview ##
def detail(request, student_id):
    student1 = get_object_or_404(Student, pk=student_id)
    courses = student1.course_set.all()

    #Caluculate each Classes's Grade
    classGrades = []
    for course in courses:
        classGrades.append( calculateClassGrade( course ) )
             
    if request.method == 'POST': # If the form has been submitted...
        form = courseAdd(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            course_to_save = form.save( commit=False) #This returns an object form the form with no student associated with it
            student1.course_set.create( course_name = course_to_save.course_name , course_code =course_to_save.course_code  )
            return HttpResponseRedirect('/GT/' + str(student_id) ) # Redirect after POST
    else:
        form = courseAdd() # An unbound form
    return render(request, 'GradeTracker/detail.html', {'student': student1 , 'form': form, \
        'courses':courses, 'activities':activities, 'subactivities':subactivities, 'grades':classGrades })

def editCourse( request, course_id=None ):
    
    ##Grab the student from the user object, if there is none return invalid login
    try:
        student = Student.objects.filter(user=request.user)[0]
    except: 
        return render(request, 'GradeTracker/invalid_login.html')

    course = get_object_or_404( Course, pk=course_id ) #Get the course to edit

    if request.method == 'POST': 			# If the form has been submitted...
        form = courseAdd(request.POST, instance=course) # A form bound to the POST data, with the course loaded
        if form.is_valid(): 				# All validation rules pass
            # Process the data in form.cleaned_data
            form.save()

            return HttpResponseRedirect('/GT/' + str(student.id) ) # Redirect after POST
    else:
        form = courseAdd(instance=course) # An unbound form
    return render(request, 'GradeTracker/editCourse.html', { 'form': form , 'course':course} )

def deleteCourse( request, course_id ):
    course = get_object_or_404( Course, pk=course_id )
    studentReturned = course.student.id
    course.delete()
    return HttpResponseRedirect( '/GT/' + str(studentReturned ) )
