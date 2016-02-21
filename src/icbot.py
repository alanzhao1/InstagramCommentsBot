#! /usr/bin/env python3

# imports
import praw
import os
import sqlite3
import logging


USER_AGENT = "InstagramCommentsBot v. BETA 1.0 by /u/whereisspacebar"

r = praw.Reddit(USER_AGENT)


class icbot:
    
    def __init__(self, username, password, limit=25):
        self.username = username
        self.password = password
        self.limit = limit


if __name__ == "__main__":
    username = os.environ.get(REDDIT_USERNAME)
    password = os.environ.get(REDDIT_PASSWORD)
    
    myBot = icBot(username, password)
