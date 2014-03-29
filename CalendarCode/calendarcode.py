import requests
import json
import time

from oauth2 import OAuthDeviceFlow

CODE_URI = 'https://accounts.google.com/o/oauth2/device/code'  
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
CLIENT_ID='453267463678-0mesdcmqj8b3m4lmc3ahv7losu7f1fe7.apps.googleusercontent.com'
CLIENT_SECRET='1RTctpITEaTLF9fGV5ZifQH1'
SCOPE='https://www.googleapis.com/auth/calendar.readonly' #Change scope (currently readonly for testing)

oauth = OAuthDeviceFlow(
	code_uri=CODE_URI,              # URI for obtaining OAuth user code
	token_uri=TOKEN_URI,            # URI for obtaining OAuth tokens
	client_id=CLIENT_ID,            # OAuth Client ID
	client_secret=CLIENT_SECRET,    # 
	scope=SCOPE
	)
token = oauth.access_token()
print( 'Returned access_token: ', token )

# Make a call to GoogleCalendarAPI

# for each class in current year
#	for each event in each class
#		eventstring = urlencode of EventName at EventPlace on Eventdate EventStart-EventEnd
#			api_uri = 'https://www.googleapis.com/calendar/v3/calendars/primary/events/quickAdd?text=' + eventstring \
#				+ '&access_token=' + token

api_uri = 'https://www.googleapis.com/calendar/v3/calendars/primary/events?' \
		+ 'access_token=' + token
		
r = requests.get(api_uri)
data = json.loads(r.content)
print data

