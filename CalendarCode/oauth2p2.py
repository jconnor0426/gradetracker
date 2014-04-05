#!/usr/bin/env python
# encoding: UTF-8
#

import sys
import pickle
import requests
import json
import time

class AuthorizationException(Exception): pass

class OAuthDeviceFlowP2():

    def __init__(self, code_uri, token_uri, client_id, client_secret, scope, access_token, token_type, expires, refresh_token, device_code, expires_in, interval):
        self._code_uri = code_uri
        self._token_uri = token_uri
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope
	self._access_token = access_token
	self._token_type = token_type
	self._expires = expires
	self._refresh_token = refresh_token
	self._device_code = device_code
	self._expires_in = expires_in
	self._interval = interval

    def authorize(self):
        print
        print "Waiting for authorization: "

	device_code = self._device_code
	expires_in = self._expires_in
	interval = self._interval

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
