#!/usr/bin/env python3.6
# !/usr/bin/env python2
from user import User
from credentials import Credential
import random
import string
import pyperclip


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
def find_credential(em_address):
    '''
    function that finds the credential
    '''
    return Credential.find_credentials(em_address)



def check_account_exist(e_address):
    '''
    function that checks if an account exist with that email and returns a boolean   
    '''
    return User.account_exist(e_address)

def check_credential_exist(e_address):
    '''
    function that checks if credential exist with the email
    '''
    return Credential.credential_exist(e_address)
        
    
def delete_credentials(credential):
    '''
    function that deletes credentials
    '''
    credential.delete_credential() 
def copy_email(email_address):
    '''
    '''
    email_address.copy_credential(email_address)    
    
def view_credential():
    '''
    a function to view various account credentials
    '''
    return Credential.display_credentials()  


    

def main():
    print("WELCOME TO PASSWORD LOCKER... what is your name")
    print("\n")
    user_name=input()
    
    print(f"hello {user_name}.choose what u would like to do")
    
    while True:
        print("Use these short codes while choosing: cc -create an account, log -login, ex -exit")
        
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
            print('\n')
        
        elif short_code == 'log':
            print("LOG IN")
            print('-'*10)
            print('\n')
            print("enter the account you created before")
            e_address=input()
            if check_account_exist(e_address):
                searched_email= find_user(e_address)
                print(f"{searched_email.name},{searched_email.email}")
                print('-'*20)
                print('\n')
                print('thank you for logging in')
                print('\n')
                
            else:
                print('the email does not exist')
                break
        
        elif short_code == "ex":
                    print("holla .......")
                    break
        
        print("Use these short codes to deal with credentials after logging in:  vc -view credentials, dc -delete credential, ac -add credential, cd -copy credential")
        print('\n')
        if short_code =='ac':
            print('ADDING CREDENTIALS ')
            print('-'*10)
            print('\n')
            print("enter the account name....")
            account_name= input()
            
            print("enter the account you created before")
            e_address=input()
            
            
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
                save_credentials(add_credential(account_name,username,new_passwd,e_address))
                print('\n')
               
                print(f"new credential {account_name} {username} {e_address} {new_passwd} created")
                print('\n')
            
                print("Use these short codes while choosing:  vc -view credentials, dc -delete credential, ac -add credential, cd -copy credential")        
        elif short_code == 'vc':
            print("VIEWING CREDENTIALS")
            print('-'*20)
            print('\n')
            if view_credential():
                print("here is a list of created credentials")
                print('\n')
                for cred in view_credential():
                    print(f"{cred.account} {cred.username} {cred.password} {cred.email}")
                    print('\n')
                    print("Use these short codes while choosing:  vc -view credentials, dc -delete credential, ac -add credential, cd -copy credential")
                    print('\n')
            else:
                
                print("you seem to have no credentials")
                print('\n')
                
               
                
        elif short_code == 'dc':
            print('DELETING CREDENTIALS')
            print('-'*10)
            print('\n')
            print('enter the credential email you want to delete')
            search_email=input()
            print(check_credential_exist(search_email))
            
            if check_credential_exist(search_email):
                searched_email = find_credential(search_email)
                print(f"{searched_email.account} {searched_email.username}")
                print(''*10)
                searched_email.delete_credential()
                print('credential deleted')
                print('\n')
                print("Use these short codes while choosing:  vc -view credentials, dc -delete credential, ac -add credential, cd -copy credential")
            else:
                print("that credential does not exist")    
                               
        
        elif short_code == 'cd':
            print('COPYING CREDENTIALS')
            print('-'*10)
            print('\n')
            print('enter the  email of a credential you want to copy')
            search_email=input()
            # print('enter the  username of a credential you want to copy')
            # search_username=input()
            print(check_credential_exist(search_email))
            
            if check_credential_exist(search_email):
                searched_email = find_credential(search_email)
                print(f"{searched_email.account} {searched_email.username}")
                print(''*10)
                searched_email.copy_credential(search_email)
                print('credential copied')
                print('\n')
                print("Use these short codes while choosing:  vc -view credentials, dc -delete credential, ac -add credential, cd -copy credential")
            else:
                print("that credential does not exist")            
            
if __name__ == '__main__':

    main()            
           