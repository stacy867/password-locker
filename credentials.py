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
    def find_by_email1(cls,e_address):
        '''
        method that takes in email and returns account that matches taht email.
        Args:
             e_address:email to search for
        Returns:
        account of person that  matches the email.
        '''
        for user in cls.credential_list:
            if user.email == e_address:
                return user     
    
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
            