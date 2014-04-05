#!/usr/bin/env python
# encoding: UTF-8
#

import sys
import pickle
import requests
import json
import time

class AuthorizationException(Exception): pass

class OAuthDeviceFlow():
    _access_token = None
    _token_type = None
    _expires = 10
    _refresh_token = None
    _device_code = None
    _expires_in = None
    _interval = None
    _user_code = None

    def __init__(self, code_uri, token_uri, client_id, client_secret, scope):
        self._code_uri = code_uri
        self._token_uri = token_uri
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope

    def authorize(self):
        r = requests.post(self._code_uri,
            data=dict(client_id=self._client_id, scope=self._scope))
        r.raise_for_status()
        response = json.loads(r.content)
        #Testing Console Code
        print "User code:", response['user_code']
        print
        print "Please go to " + str(response['verification_url'])
        print
        print "You will be prompted for authorization."

	self._user_code = response['user_code']
        self._device_code = response['device_code']
        self._expires_in = int(response['expires_in'])
        self._interval = int(response['interval'])

    def refresh_token(self):
        r = requests.post(self._token_uri,
            data=dict(client_id=self._client_id,
                      client_secret=self._client_secret,
                      refresh_token=self._refresh_token,
                      grant_type='refresh_token'))
        r.raise_for_status()  #Raises stored :class:`HTTPError`, if one occurred.
        response = json.loads(r.content)
        if response.get("error"):
            raise AuthorizationException("Error: " + response['error'])
        else:
            self._access_token = response['access_token']
            self._token_type = response['token_type']
            self._expires = int(response['expires_in']) + time.time()
        
    def access_token(self):
        '''Get an access token.
        
        If the token has expired, fetch a new token with refresh token. If
        refresh token is not known, go through authorization process.
        '''
        if not self._refresh_token:
            self.authorize()
        if time.time() > self._expires:
            self.refresh_token()
        return self._access_token
