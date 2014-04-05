import requests
import json
import time
import sys

from oauth2p2 import OAuthDeviceFlowP2

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

api_uri = 'https://www.googleapis.com/calendar/v3/colors?' \
		+ 'access_token=' + token
		
r = requests.get(api_uri)
data = json.loads(r.content)
print(data)
