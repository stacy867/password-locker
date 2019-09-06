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
        Credential.credential_list.append({'account': self.account, 'username':self.username, 'password':self.password, 'email':self.email})
        
        
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
            