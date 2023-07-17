# Tools
import inspect
import unittest
import yaml
# Library
from MostImportant50.APILayer.API import *
from MostImportant50.tools.logs import LogInformation


class VerifyloginPage(unittest.TestCase, LogInformation):

    loggingData = ""

    def setUp(self):
        self.loggingData = LogInformation(namefile=__class__.__name__)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Class Name - " + __class__.__name__)
        self.driver = web_driver()
        self.driver.fullscreen_window()
        self.username = ["NAME", "login[username]"]
        self.password = ["NAME",  "login[password]"]
        self.SubmitBtn = ["ID", "send2"]
        self.mainmenu = ["CLASS_NAME", "ui.nav.items"]

    # real data from yaml file
    def readyaml(self, toFetchTestData):
        with open('../yaml/config_magento.yaml', 'r') as file:
            TestData = yaml.safe_load(file)
            self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message=TestData[toFetchTestData])
        return TestData[toFetchTestData]

    def test_check_login(self):
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******Starting test - test_check_login********")
        driver = self.driver
        TestData = self.readyaml(toFetchTestData=inspect.currentframe().f_code.co_name)

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="url - " + TestData['url'])
        driver.get(TestData['url'])

        self.assertIn(TestData['url'], driver.current_url)

        presence_of_element_located(self.loggingData, driver, __class__.__name__, self.username, timeout=5)
        
        username_textbox = find_element(driver, self.username)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="username - " + TestData['username'])
        username_textbox.send_keys(TestData['username'])

        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="password - " + TestData['password'])
        password_textbox = find_element(driver, self.password)
        password_textbox.send_keys(TestData['password'])

        SignIn_button = find_element(driver, self.SubmitBtn)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="Press Submit Button")
        SignIn_button.submit()

        presence_of_element_located(self.loggingData, driver, __class__.__name__, self.mainmenu,timeout=10)
        actualUrl=driver.current_url
        expectedUrl= TestData['expected']
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="expectedUrl - " + expectedUrl)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="actualUrl - " + actualUrl)
        self.assertIn(expectedUrl, actualUrl)
        self.loggingData.TEST_INFORMATION(namefile=__class__.__name__, message="*******End test - test_check_login********")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
