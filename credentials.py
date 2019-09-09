import pyperclip
class Credential:
    
    credential_list= []
    """
    class that generates credentials.
    """
    
    def __init__(self, account, username, password,email):
        self.account = account
        self.username = username
        self.password = password
        self.email= email
        # Credential.credential_list.append({'account': self.account, 'username':self.username, 'password':self.password, 'email':self.email})
        
        
    def save_credential(self):
        '''
        save_credential saves account in the credentials list
        '''
        Credential.credential_list.append(self)    
        
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the list of credentials created
        '''
        return cls.credential_list
    
     
    
    @classmethod
    def credential_exist(cls,e_address):
        '''
        method that checks if account exists from the account created
        
        Args:
             e_address: email to search if it exists
        Returns:
            Boolean:True or false depending if the email exists
        '''
        for credential in cls.credential_list:
            print(credential.email)
           
            if credential.email == e_address:
                return True         
            else:
                return False            
    
    @classmethod
    def find_credentials(cls,em_address):
        '''
        method that takes in the username and returns credentials that matches the username
        
        Args:
             username: username of the credential
        Returns:
                credentials that matches the username
        '''
        
        for newuser in cls.credential_list:
            if newuser.email == em_address:
                return newuser           
    def delete_credential(self):
        '''
        a function that deletes a credential
        '''
        Credential.credential_list.remove(self)
    
    
    @classmethod
    def copy_credential(cls,email):
        email_found = Credential.find_credentials(email) 
        pyperclip.copy(email_found.email) 
        # pyperclip.copy(email.found.username)  