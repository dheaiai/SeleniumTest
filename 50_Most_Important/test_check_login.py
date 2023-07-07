#Tools
import unittest
import yaml
import time
from tools.logs import LogInformation
import logging
#from logs import LogInformation
#Selenium based
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Verifyloginfunctionalitywithvalidcredentials(unittest.TestCase, LogInformation):

    def setUp(self):
        self.TEST_INFORMATION(namefile=__class__.__name__, message="Class Name - " + __class__.__name__)
        self.driver = webdriver.Chrome()
        self.data = self.readyaml(__class__.__name__)

    def readyaml(self, toFetchTestData):
        with open('yaml/config.yaml', 'r') as file:
            TestData = yaml.safe_load(file)
            self.TEST_INFORMATION(namefile=__class__.__name__, message=TestData[toFetchTestData])
        return TestData[toFetchTestData]

    def test_check_login(self):
        driver = self.driver
        TestData = self.data

        self.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn("OrangeHRM", driver.title)

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.NAME, "username"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            logging.error("Timed out waiting for page to load")

        username_textbox = driver.find_element(By.NAME, "username")
        self.TEST_INFORMATION(namefile=__class__.__name__, message="username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        self.TEST_INFORMATION(namefile=__class__.__name__, message="password - " + TestData['password'])
        password_textbox = driver.find_element(By.NAME, "password")
        password_textbox.send_keys(TestData['password'])

        SignIn_button = driver.find_element(By.CLASS_NAME, "oxd-button")
        SignIn_button.submit()

        timeout = 10
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "a.oxd-main-menu-item"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            self.TEST_INFORMATION(namefile=__class__.__name__, message="Timed out waiting for page to load")

        actualUrl=driver.current_url
        expectedUrl= TestData['expected']
        self.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl - " + expectedUrl)
        self.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl - " + actualUrl)
        self.assertIn(expectedUrl, actualUrl)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
