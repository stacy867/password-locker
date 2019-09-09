class User:
    '''
    class that generates user information
    '''
    
    user_list =[]
    
    def __init__(self,name,passwd,email):
        self.name = name
        self.passwd = passwd
        self.email= email
        # User.user_list = {'name':self.name,'password': self.passwd,'email': self.email}
    @classmethod    
    def check_user(cls,name,passwd,email):
        '''
        '''
        current_user=''
        for user in User.user_list:
            if(user.name == name and passwd == passwd):
                current_user = user.name
                return current_user    
        
    def save_user(self):
        '''
        save_user saves account in the credentials list
        '''
        User.user_list.append(self) 
    
    @classmethod
    def find_by_email(cls,e_address):
        '''
        method that takes in email and returns account that matches taht email.
        Args:
             e_address:email to search for
        Returns:
        account of person that  matches the email.
        '''
        for user in cls.user_list:
            if user.email == e_address:
                return user     
         
        
    @classmethod
    def account_exist(cls,e_address):
        '''
        method that checks if account exists from the account created
        
        Args:
             e_address: email to search if it exists
        Returns:
            Boolean:True or false depending if the email exists
        '''
        for user in cls.user_list:
            if user.email == e_address:
                return True         
        
        return False