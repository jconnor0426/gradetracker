from django import forms 
from django.core.validators import MaxValueValidator, MinValueValidator

class courseAdd(forms.Form):
    courseName = forms.CharField(max_length=200)
    courseCode = forms.CharField( max_length=200)

class activityAdd(forms.Form):
    activityName = forms.CharField(max_length=200)
    activityWeight = forms.FloatField(validators = [MinValueValidator(0.00), MaxValueValidator(1.00)])
