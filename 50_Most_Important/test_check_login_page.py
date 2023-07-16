# Tools
import unittest
import yaml
import inspect
from tools.logs import LogInformation
# import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VerifyloginPage(unittest.TestCase, LogInformation):

    loggingData = ""

    def setUp(self):
        self.loggingData = LogInformation(namefile=__class__.__name__)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Class Name - " + __class__.__name__)
        self.driver = webdriver.Chrome()
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.SubmitBtn = (By.CLASS_NAME, "oxd-button")
        self.mainmenu = (By.CSS_SELECTOR, "a.oxd-main-menu-item")
        self.InvalidCredentials = (By.XPATH, '//*[text()="Invalid credentials"]')
        self.ForgotPasswordBtn = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
        self.ForgotPasswordLevel = (By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title")
        self.ResetPasswordBtn = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset")
        self.ResetLinkSent = (By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title")

    # real data from yaml file
    def readyaml(self, toFetchTestData):
        with open('yaml/config.yaml', 'r') as file:
            TestData = yaml.safe_load(file)
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message=TestData[toFetchTestData])
        return TestData[toFetchTestData]

    def test_check_login(self):
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******Starting test - test_check_login********")
        driver = self.driver
        TestData = self.readyaml(toFetchTestData=inspect.currentframe().f_code.co_name)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn("OrangeHRM", driver.title)

        timeout = 5
        try:
            element_present = EC.presence_of_element_located(self.username)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        
        username_textbox = driver.find_element(*(self.username))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="password - " + TestData['password'])
        password_textbox = driver.find_element(*(self.password))
        password_textbox.send_keys(TestData['password'])

        SignIn_button = driver.find_element(*(self.SubmitBtn))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press Submit Button")
        SignIn_button.submit()

        timeout = 10
        try:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Wait page to be load completely")
            element_present = EC.presence_of_element_located(self.mainmenu)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        actualUrl=driver.current_url
        expectedUrl= TestData['expected']
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl - " + expectedUrl)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl - " + actualUrl)
        self.assertIn(expectedUrl, actualUrl)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******End test - test_check_login********")


    def test_check_login_failed(self):
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******Starting test - test_check_login_failed********")
        driver = self.driver
        TestData = self.readyaml(toFetchTestData=VerifyloginPage.test_check_login_failed.__name__)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn("OrangeHRM", driver.title)

        timeout = 5
        try:
            element_present = EC.presence_of_element_located(self.username)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        username_textbox = driver.find_element(*(self.username))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="password - " + TestData['password'])
        password_textbox = driver.find_element(*(self.password))
        password_textbox.send_keys(TestData['password'])

        SignIn_button = driver.find_element(*(self.SubmitBtn))
        SignIn_button.submit()

        timeout = 10
        try:
            element_present = EC.presence_of_element_located(self.mainmenu)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        actualUrl=driver.current_url
        expectedUrl= TestData['expected']
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl - " + expectedUrl)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl - " + actualUrl)
        self.assertIn(expectedUrl, actualUrl)

        
        InvalidCredentials = driver.find_element(*(self.InvalidCredentials))
        actualString=InvalidCredentials.text
        expectedString= TestData['expected2']
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedString - " + expectedString)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualString - " + actualString)
        self.assertIn(expectedString, actualString)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******End test - test_check_login_failed********")


    def test_check_forgot_password(self):
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******Starting test - test_check_forgot_password********")
        driver = self.driver
        TestData = self.readyaml(toFetchTestData=VerifyloginPage.test_check_forgot_password.__name__)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn("OrangeHRM", driver.title)

        timeout = 5
        try:
            element_present = EC.presence_of_element_located(self.username)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        ForgotPassword = driver.find_element(*(self.ForgotPasswordBtn))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press - Forgot your password?")
        ForgotPassword.click()

        try:
            element_present = EC.presence_of_element_located(self.ForgotPasswordLevel)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="reseturl-" + TestData['reseturl'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualurl-" + driver.current_url)
        self.assertIn(TestData['reseturl'], driver.current_url)

        username_textbox = driver.find_element(*(self.username))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Enter username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        ResetPassword = driver.find_element(*(self.ResetPasswordBtn))
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press Reset Password Button")
        ResetPassword.submit()
        self.assertIn(TestData['expected'], driver.current_url)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl after pressing ResetPassword - "+ TestData['expected'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl after pressing ResetPassword - "+ driver.current_url)

        try:
            element_present = EC.presence_of_element_located(self.ResetLinkSent)
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        expected2 = driver.find_element(*(self.ResetLinkSent))

        self.assertIn(TestData['expected2'], expected2.text)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedString on sendPasswordReset is - "+ TestData['expected2'])
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualString on sendPasswordReset is - "+ expected2.text)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="******* End test - test_check_forgot_password ********")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
