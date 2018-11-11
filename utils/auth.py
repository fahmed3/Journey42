import os, hashlib
from flask import session
from utils import database

#encrypts passwords
def encrypt(password):
    return hashlib.sha224(password.encode('utf-8')).hexdigest()

#creates a new user
def new_user(username, password):
    return database.adduser(username, encrypt(password))

def update_pass(username, password):
    return database.change_password(username, encrypt(password))

#checks password
def verify(username, password):
    # print (encrypt(password))
    # print (database.get_password(username))
    return encrypt(password) == database.get_password(username)

#checks username
def user_exists(username):
    return database.get_password(username) is not None

#checks to see if logged in
def logged_in():
    return 'username' in session

#creates a new session if username and password match
def login(username, password):
    if(verify(username,password)):
        session['username'] = username
        return True
    else:
        return False

#removes login cookie
def logout():
    if logged_in():
        session.pop('username')
