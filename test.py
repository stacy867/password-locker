import unittest #importing the unittest module
from credentials import Credential #importing the credentials class
from user import User #importing the user class from user file

## user test
class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user  class behaviours.
    
    Arguments:
              unittest.TestCase: TestCase class that helps in creating test cases.
    """
    
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_user= User('stacy', '1234', 'stacymurenzi@gmail.com')#create a user object
        
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name,"stacy")
        self.assertEqual(self.new_user.passwd,"1234")
        self.assertEqual(self.new_user.email,"stacymurenzi@gmail.com")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''    
    
    def test_save_user(self):
        '''
        save_acct test case is to test if the account is being saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)    
        
 ## credentials test
 
class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user  class behaviours.
    
    Arguments:
              unittest.TestCase: TestCase class that helps in creating test cases.
    """
    
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_credential= Credential('instagram','stacy', '1234', 'stacymurenzi@gmail.com')#create a user object
        
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"instagram")
        self.assertEqual(self.new_credential.username,"stacy")
        self.assertEqual(self.new_credential.password,"1234")  
        self.assertEqual(self.new_credential.email,"stacymurenzi@gmail.com")      
        
    def test_save_credential(self):
        '''
        save_acct test case is to test if the account is being saved
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),3)
    
          
if __name__ == '__main__':
    unittest.main()        
              
    
    