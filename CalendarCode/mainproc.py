import requests
import json
import time
import subprocess

from oauth2 import OAuthDeviceFlow

CODE_URI = 'https://accounts.google.com/o/oauth2/device/code'  
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
CLIENT_ID='453267463678-0mesdcmqj8b3m4lmc3ahv7losu7f1fe7.apps.googleusercontent.com'
CLIENT_SECRET='1RTctpITEaTLF9fGV5ZifQH1'
SCOPE='https://www.googleapis.com/auth/calendar.readonly'

oauth = OAuthDeviceFlow(
	code_uri=CODE_URI,              # URI for obtaining OAuth user code
	token_uri=TOKEN_URI,            # URI for obtaining OAuth tokens
	client_id=CLIENT_ID,            # OAuth Client ID
	client_secret=CLIENT_SECRET,    # 
	scope=SCOPE
	)

oauth.authorize()
argumentstring = str(CODE_URI)+" "+str(TOKEN_URI)+" "+str(CLIENT_ID)+" "+str(CLIENT_SECRET)+" "+str(SCOPE)+" "+str(oauth._access_token)+" "+str(oauth._token_type)+" "+str(oauth._expires)+" "+str(oauth._refresh_token)+" "+str(oauth._device_code)+" "+str(oauth._expires_in)+" "+str(oauth._interval)
subprocess.Popen(["nohup","python","spawnedproc.py",argumentstring])
print("done")



