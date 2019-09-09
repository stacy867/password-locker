import unittest #importing the unittest module

from user import User #importing the user class from user file
from credentials import Credential #importing the credentials class

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
        User.user_list= []   
    
    def test_save_user(self):
        '''
        save_acct test case is to test if the account is being saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 
        
    def test_account_exist(self):
        '''
        tests to check if we can return a boolean if we cannot find the account
        '''
        
        self.new_user.save_user()
        test_user=User("murenzi","12345","murenzi@gmail.com")#new user
        test_user.save_user()
        
        email_exist = User.find_by_email("murenzi@gmail.com")
        self.assertTrue(email_exist)
    
    def test_check_user(self):
        '''
        '''
        self.new_user = User('stacy','1234','stacymurenzi@gmail.com')
        self.new_user.save_user()
        user1= User('sss','1234','sss@gmail.com')
        user1.save_user()
        
        for user in User.user_list:
            if user.name == user1.name and user.passwd == user1.passwd:
                current_user = user.name
                # return current_user
                self.assertEqual(current_user,User.check_user(user1.name,user1.passwd,user1.email))      
        

          
if __name__ == '__main__':
    unittest.main()        
              
    
    