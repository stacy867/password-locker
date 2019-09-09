 ## credentials test
import unittest #importing the unittest module
from credentials import Credential
from user import User #importing the user class from user file




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
        
    
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        ''' 
        Credential.credential_list= []      
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
        self.assertEqual(len(Credential.credential_list),1)
        
    def test_display_credentials(self):
        '''display_credential test case that returns  list of credentials
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)    
    
    def test_find_credentials(self):
        '''
        test to check if we can find a credential by username and display information
        '''
        
        self.new_credential.save_credential()
        test_credential= Credential("Test","username", "123456","test@user.com")#new credential
        test_credential.save_credential()
        
    def test_credential_exist(self):
        '''
        test to check if credential exist
        '''
        self.new_credential.save_credential()
        test_credential= Credential("test","stacy","123678","test@gmail.com")
        test_credential.save_credential()
        
        credential_exists = Credential.credential_exist("test@gmail.com")
        
        self.assertTrue(credential_exist) 
        
    def test_delete_credential(self):
        '''
        test to test if a credential has been removed
        '''
        self.new_credential.save_credential()
        test_credential= Credential("Test","username", "123456","test@user.com")
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
              
import pyperclip

    
def test_copy_credential(self):
        '''
        test to check if credentials have been copied
        '''
        self.new_credential.save_credential()
        Credential.copy_credential("test@user")
        self.assertEqual(self.new_credential.email,pyperclip.paste())
        
            
if __name__ == '__main__':
    unittest.main()        