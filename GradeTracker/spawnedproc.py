import requests
import json
import time
import sys
import urllib

'''
from subprocess import call

sys.path.append('/home/jconnor/GradeTracker/gradetracker/GradeTracker')
sys.path.append('/home/jconnor/GradeTracker/gradetracker')
from models import Student, Course, Graded_Activities, SubGraded_Activities
call(['pwd'])
'''

from oauth2p2 import OAuthDeviceFlowP2

#from django.contrib import auth
#from gradetracker.GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities

arglist = sys.argv[1].split()

oauthp2 = OAuthDeviceFlowP2(
	code_uri=arglist[0],            # URI for obtaining OAuth user code
	token_uri=arglist[1],           # URI for obtaining OAuth tokens
	client_id=arglist[2],           # OAuth Client ID
	client_secret=arglist[3],    # 
	scope=arglist[4],
	access_token=arglist[5],
	token_type=arglist[6],
	expires=arglist[7],
	refresh_token=arglist[8],
	device_code=arglist[9],
	expires_in=arglist[10],
	interval=float(arglist[11])
	)

oauthp2.authorize()
token = oauthp2.access_token()
print( 'Returned access_token: ', token )

# Make a call to GoogleCalendarAPI

current_student = Student.objects.filter(user=request.user)[0]
courses = Course.objects.filter(student=current_student.id)

for course in courses:
    for activity in course.graded_activities_set.all:
        year = activity.grade_due_date.year
        month = activity.grade_due_date.month
        day = activity.grade_due_date.day
        name = activity.activity_name
        eventstring = str(activity_name) + " on " + str(month) + "/" + str(day) + "/" + str(year)
        r = requests.get(api_uri)
	data = json.loads(r.content)
	print(data)
	
api_uri = 'https://www.googleapis.com/calendar/v3/calendars/primary/events/quickAdd?text=' \
                + urllib.urlencode(eventstring) + "&access_token=" + token
#api_uri = 'https://www.googleapis.com/calendar/v3/colors?' \
#		+ 'access_token=' + token
		
#r = requests.get(api_uri)
#data = json.loads(r.content)
#print(data)
