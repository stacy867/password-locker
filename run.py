#!/usr/bin/env python3
#!/usr/bin/env python2
from user import user
from credentials import Credential

def create account(username,passwd,email):
    '''
    function that creates an ccount for a user
    '''
    new_user= User(username,passwd,email)
    return new_user

def save_acct(credential):
    '''
    function that saves credentials
    '''
    credential.save_acct()
    
def delete_acct(credential):
    '''
    function that deletes credentials
    '''
    credential.delete_acct() 
    
    
def view_acct():
    '''
    a function to view various account credentials
    '''
    return Credential.view_acct()      