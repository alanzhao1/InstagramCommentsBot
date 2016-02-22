#! /usr/bin/env python3

# imports
import praw
import os
import sqlite3
import logging
import json
import re
import requests

from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token
from settings import user_agent, scopes

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError


INSTAGRAM_REGEX = re.compile('http[s]?://instagram.com/p/\S+|http[s]?://www.instagram.com/p/\S+')

# TODO: logging setup
loglevel = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(level=loglevel)
log = logging.getLogger('icbot')

# reddit api setup
reddit_client = praw.Reddit(user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key = app_key,
        app_secret = app_secret, access_token = access_token,
        scopes = scopes, refresh_token = refresh_token)

# open database
icbotconn = sqlite3.connect(icbot.db)
dbcursor = icbotconn.cursor()

class Instagram_Comment:

    def __init__(self, comment_regex, comment_id):
        self.comment_regex = comment_regex
        self.comment_id = comment_id
        self_media_id = []

    # Set this as a seperate function so we can limit unnecessary calls to 
    # Instagram's API
    def set_media_id (self):
        for ig_url in comment_id:
            r = requests.get("http://api.instagram.com/oembed?url=%s", %ig_url)
            self_media_id.append(json.loads(r.text)[media_id])    
            
class ICBot:
    
    def __init__(self,limit=25):
        # TODO: Rate limit under OAuth2 
        self.limit = limit
   
    def run():
        log.info("Running ")

        all_comments = r.get_comments('all')
        insta_comments = []

        for comment in all_comments:
            comment_re = re.findall(INSTAGRAM_REGEX, str(comment.body))
            if len(comment_re) > 0
                insta_comments.append(Instagram_Comment(comment_re, comment.id))

        for comment in insta_comments:
            if (str(comment.comment_id),) in dbcursor.execute("SELECT ID FROM reddit"):
                logging.info("Already processed submission " + str(submission.id))
                continue:
            else:
                comment.set_media_id() 
                
                # TODO: use InstagramAPI to find URL, possibly author and 
                # comment in the future
                

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


