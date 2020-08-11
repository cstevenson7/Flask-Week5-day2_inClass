import os
basedir = os.path.abspath(os.path.dirname(__file__))  # always need these two commands

#windows = D:\Coding_Temple\week5\day1\

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess..'
    #use sql lite if you can't find the other db connection  backend connection
