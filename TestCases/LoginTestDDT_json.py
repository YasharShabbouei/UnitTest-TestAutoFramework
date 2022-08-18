import unittest
from selenium import webdriver
import sys
sys.path.append(r"C://Users//yasha//OneDrive//Desktop//Python test//Unittest_POM")
from PageObjects.LoginPageElements import LoginPage
import HtmlTestRunner
import time
from ddt import ddt, data, unpack, file_data

@ddt
class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data(r"C:\Users\yasha\OneDrive\Desktop\Python test\Unittest_POM\testData\testData.json")
    def test_Login(self, username, password):
        loginObject = LoginPage(self.driver)
        loginObject.setUserName(username)
        loginObject.setUserPassword(password)
        loginObject.clickLogin()
        time.sleep(5)
        self.assertEqual('Dashboard / nopCommerce administration', self.driver.title, "webpage title is not matching")
        loginObject.clickLogout()
        time.sleep(5)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\yasha\OneDrive\Desktop\Python test\Unittest_POM\ReportFolder"))



