import os
import logging
import httplib2

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from googleapi.models import CredentialsModel
from googleapi import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from GradeTracker.models import Student, Course, Graded_Activities, SubGraded_Activities, Templates

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope=
      'https://www.googleapis.com/auth/calendar',
    redirect_uri='http://imgkee.io:8000/goog/oauth2callback/')


@login_required
def index(request):
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  credential = storage.get()
  if credential is None or credential.invalid == True:
    FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                   request.user)
    authorize_url = FLOW.step1_get_authorize_url()
    return HttpResponseRedirect(authorize_url)
  else:
    http = httplib2.Http()
    http = credential.authorize(http)
    service = build('calendar', 'v3', http=http)

    #See if general calendar stuff will work. If it doesn't than we need to reauth
    try:
      calendar = service.events().list(calendarId='primary').execute()
    except:
      FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                   request.user)
      authorize_url = FLOW.step1_get_authorize_url()
      return HttpResponseRedirect(authorize_url)

    #Now do the real calendar work

    #Get a user's activities:
    student = Student.objects.filter( user=request.user ) [0]

    #build events to export
    export_list = []
    for course in student.course_set.all():
      for activity in course.graded_activities_set.all():
        export_list.append( activity )

    activitylist = export_list

    
    #activitylist = calendar[ 'summary' ]


  return render_to_response('plus/welcome.html', {"activitylist":activitylist} )


@login_required
def auth_return(request):
  if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'],
                                 request.user):
    return  HttpResponseBadRequest()
  credential = FLOW.step2_exchange(request.REQUEST)
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  storage.put(credential)
  return HttpResponseRedirect("/goog")
