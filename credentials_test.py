 ## credentials test
import unittest #importing the unittest module
from credentials import Credential #importing the credentials class


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
        self.assertEqual(len(Credential.credential_list),2)

if __name__ == '__main__':
    unittest.main()        