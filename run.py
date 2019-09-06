#!/usr/bin/env python3.6
# !/usr/bin/env python2
from user import User
from credentials import Credential
import random
import string


def randomString(stringLength):
    '''
    Generate a random string 
    '''
    letters = string.ascii_letters
    return ''.join(random.choice(letters)for i in range(stringLength))

def create_account(name,passwd,email):
    '''
    function that creates an ccount for a user
    '''
    new_user= User(name,passwd,email)
    return new_user

def add_credential(account, username, password,email):
    '''
    function that adds credentials
    '''
    new_cred= Credential(account, username, password,email)
    return new_cred



def save_users(user):
    '''
    function that saves credentials
    '''
    
    user.save_user()

def save_credentials(credential):
    '''
    function that saves credentials
    '''
    credential.save_credential()
       

def find_user(e_address):
    '''
    function that finds a user by email and returns the email
    '''
    return User.find_by_email(e_address)

def check_account_exist(e_address):
    '''
    function that checks if an account exist with that email and returns a boolean   
    '''
    return User.account_exist(e_address)
    
    
    
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
        print("Use these short codes while choosing: cc -create an account, vc -view credentials, dc -delete credential, ac -add credential, fc -find account")
        
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
        
        
        elif short_code =='ac':
            
            print("enter the account name....")
            account_name= input()
            
            print("enter the account you created before")
            e_address=input()
            if check_account_exist(e_address):
                searched_email= find_user(e_address)
                print(f"{searched_email.name},{searched_email.email}")
                print('-'*20)
            else:
                print('the email does not exist')  
            
            print("enter username....")
            username= input()      
            
            print("choose if you want to be generated a password or not: cp -create ur password, gp -app generates password for you")
            choice =input().lower()
            if choice == 'cp':
                print("enter password")
                new_passwd=input()
                save_credentials(add_credential(account_name,e_address,username,new_passwd))
                print('\n')
                print(f"new credential {account_name} {username} {e_address} {new_passwd}") 
                
            
            else:
                print("your new generated password is:")
                new_passwd= randomString(5)
                print(new_passwd)
                save_credential(add_credential(account_name,e_address,username,new_passwd))
            print('\n')
            print(f"new credential {account_name} {username} {e_address} {new_passwd}")
                
                
            
if __name__ == '__main__':

    main()            
           