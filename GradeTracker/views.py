# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from GradeTracker.models import Student, Course

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'GradeTracker/detail.html', {'student': student})
def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list }
    return render( request, 'GradeTracker/index.html', context )  

