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
        print "Please go to: ", response['verification_url']
        print
        print "You will be prompted for authorization."
        print
        print "Waiting for authorization: "
        device_code = response['device_code']
        expires_in = int(response['expires_in'])
        interval = int(response['interval'])
        start = time.time()
        while time.time() - start < expires_in:
            time.sleep(interval)
            r = requests.post(self._token_uri,
                data=dict(client_id=self._client_id,
                          client_secret=self._client_secret,
                          code=device_code,
                          grant_type='http://oauth.net/grant_type/device/1.0'))
            r.raise_for_status()  #Raises stored :class:`HTTPError`, if one occurred.
            response = json.loads(r.content)
            # Continue if auth pending, break on error, process if no error.
            if response.get("error") == "authorization_pending":
                print '.'
                continue
            elif response.get("error"):
                raise AuthorizationException("Error: " + response['error'])
            else:
                self._access_token = response['access_token']
                self._token_type = response['token_type']
                self._expires = int(response['expires_in']) + time.time()
                self._refresh_token = response['refresh_token']
                break

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
