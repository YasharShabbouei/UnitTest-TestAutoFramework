import unittest
from selenium import webdriver
import sys
sys.path.append(r"C://Users//yasha//OneDrive//Desktop//Python test//Unittest_POM")
sys.path.append(r"C://Users//yasha//OneDrive//Desktop//Python test//Unittest_POM//utilities")

from PageObjects.LoginPageElements import LoginPage
from utilities.utils import read_data_from_excel
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

    @data(*read_data_from_excel(r"C:\Users\yasha\OneDrive\Desktop\Python test\Unittest_POM\testData\testExcel.xlsx", "Sheet1"))
    @unpack
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



