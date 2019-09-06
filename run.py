#!/usr/bin/env python3.6
# !/usr/bin/env python2
from user import User
from credentials import Credential

def create_account(name,passwd,email):
    '''
    function that creates an ccount for a user
    '''
    new_user= User(name,passwd,email)
    return new_user

def save_users(user):
    '''
    function that saves credentials
    '''
    
    user.save_user()
    
def delete_credential(credential):
    '''
    function that deletes credentials
    '''
    credential.delete_credential() 
    
    
def view_credential():
    '''
    a function to view various account credentials
    '''
    return Credential.view_credential()  


def main():
    print("WELCOME TO PASSWORD LOCKER... what is your name")
    print("\n")
    user_name=input()
    
    print(f"hello {user_name}.choose what u would like to do")
    
    while True:
        print("Use these short codes while choosing: cc -create an account, vc -view credentials, dc -delete credential")
        
        short_code=input().lower()
        
        if short_code=='cc':
            print("New Account")
            print('\n')
            
            print('username....')
            names= input()
            
            
            print('password....')
            passwds= input()
            
            print('email....')
            emails= input()
            
            
            save_users(User(names,passwds,emails))
            print('\n')
            print(User.user_list)
            print(f"New Account {names} {passwds} {emails}  created")
            
if __name__ == '__main__':

    main()            
           