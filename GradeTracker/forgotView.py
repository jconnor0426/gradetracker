from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery --> method for people hacking into website
from GradeTracker.models import User, Student, Course, Graded_Activities, SubGraded_Activities, Templates
from GradeTracker.forms import courseAdd, activityAdd, subactivityAdd, MyRegistrationForm, forgotPassword
from django.core.mail import send_mail
import random
import string

def forgot(request):
    if request.method == 'POST': # If the form has been submitted...
        form = forgotPassword(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            email = form.cleaned_data['email']
            # Process the data in form.cleaned_data
            user = User.objects.filter(email=email)[0]
            if user is not None:
                form.save()
                new_password = str(id_generator())
		user.set_password(new_password)
                send_mail("Your PW", new_password, "admin@GradeTracker.com", [email])
                return HttpResponseRedirect('/GT/' + "validEmail")
            else:
                return HttpResponseRedirect('/GT/' + "forgot")
    else:
        form = forgotPassword()
    return render(request, 'GradeTracker/forgot.html', {'form':form})
        
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
