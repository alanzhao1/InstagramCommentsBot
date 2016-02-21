#! /usr/bin/env python3

# imports
import praw
import os
import sqlite3
import logging
import json

from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token
from settings import user_agent, scopes

# TODO: logging setup
#loglevel = logging.DEBUG if DEBUG else logging.INFO
#logging.basicConfig(level=loglevel,
#log = logging.getLogger('icbot')

# reddit api setup
reddit_client = praw.Reddit(user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key = app_key,
        app_secret == app_secret, access_token = access_token,
        scopes = scopes, refresh_token = refresh_token)

class ICBot:
    
    def __init__(self,limit=25):
        self.limit = limit
   
    def run():
        pass

    def _setup(self):
        
        self.issetup = True
        

if __name__ == "__main__":
    
    icbot = ICBot()

    try:
        while True:
            try:
                icbot.run()
            except RECOVERABLE_EXEC as e:
                pass
                # TODO: handle errors via logger
    except KeyboardInterrupt:
        pass


