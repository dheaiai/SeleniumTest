#Tools
import unittest
import yaml
import time
from tools.logs import LogInformation
#import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerifyloginfunctionalityForgotPassword(unittest.TestCase, LogInformation):

    loggingData=""

    def setUp(self):
        self.loggingData = LogInformation(namefile=__class__.__name__)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Class Name - " + __class__.__name__)
        self.driver = webdriver.Chrome()
        self.data = self.readyaml(__class__.__name__)

    def readyaml(self, toFetchTestData):
        with open('yaml/config.yaml', 'r') as file:
            TestData = yaml.safe_load(file)
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message=TestData[toFetchTestData])
        return TestData[toFetchTestData]

    def test_check_forgot_password(self):
        driver = self.driver
        TestData = self.data

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn("OrangeHRM", driver.title)

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.NAME, "username"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        ForgotPassword = driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press - Forgot your password?")
        ForgotPassword.click()

        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="reseturl-" + TestData['reseturl'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualurl-" + driver.current_url)
        self.assertIn(TestData['reseturl'], driver.current_url)

        username_textbox = driver.find_element(By.NAME, "username")
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Enter username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        ResetPassword = driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset")
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press Reset Password Button")
        ResetPassword.submit()
        self.assertIn(TestData['expected'], driver.current_url)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl after pressing ResetPassword - "+ TestData['expected'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl after pressing ResetPassword - "+ driver.current_url)

        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        expected2 = driver.find_element(By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title")

        self.assertIn(TestData['expected2'], expected2.text)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedString on sendPasswordReset is - "+ TestData['expected2'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualString on sendPasswordReset is - "+ expected2.text)
        



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
