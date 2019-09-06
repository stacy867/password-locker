#!/usr/bin/env python3
#!/usr/bin/env python2
from user import User
from credentials import Credential

def create_account(username,password,email,account):
    '''
    function that creates an ccount for a user
    '''
    new_user= Credential(username,password,email,account)
    return new_user

def save_credential(credential):
    '''
    function that saves credentials
    '''
    credential.save_credential()
    
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
            username= input()
            
            print('social media platform....')
            account= input()
            
            print('password....')
            password= input()
            
            print('email....')
            email= input()
            
            
            save_credential(create_account(username,password,email,account))# create and save account
            print('\n')
            print(f"New Account {username} {password} {email} {account} created")
            
if __name__ == '__main__':

    main()            
           