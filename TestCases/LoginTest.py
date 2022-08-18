import unittest
from selenium import webdriver
import sys
sys.path.append(r"C://Users//yasha//OneDrive//Desktop//Python test//Unittest_POM")
from PageObjects.LoginPageElements import LoginPage
import HtmlTestRunner
import time



class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Login(self):
        loginObject = LoginPage(self.driver)
        loginObject.setUserName(self.username)
        loginObject.setUserPassword(self.password)
        loginObject.clickLogin()
        time.sleep(5)
        self.assertEqual('Dashboard / nopCommerce administration', self.driver.title, "webpage title is not matching")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\yasha\OneDrive\Desktop\Python test\Unittest_POM\ReportFolder"))
