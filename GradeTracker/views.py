# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from GradeTracker.models import Student, Course
from GradeTracker.forms import courseAdd

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

