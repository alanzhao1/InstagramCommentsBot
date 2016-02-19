#! /usr/bin/env python3

# imports
import praw
import os
import sqlite3
import logging


class icbot:
    
    def __init__(self, username, password, limit=25):
        self.username = username
        self.password = password
        self.limit = limit


if __name__ == "__main__":
    username = os.environ.get(REDDIT_USERNAME)
    password = os.environ.get(REDDIT_PASSWORD)
    
    myBot = icBot(username, password)
