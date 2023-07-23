# Tools
import inspect
import time

import pytest
import pytest_html

import yaml
# Library
from APILayer.API import *
from tools.logs import LogInformation

# real data from yaml file
def readyaml(loggingData, toFetchTestData):
    with open('yaml/config_magento.yaml', 'r') as file:
        TestData = yaml.safe_load(file)
        loggingData.TEST_INFORMATION(namefile=inspect.currentframe().f_code.co_name, message=TestData[toFetchTestData])
    return TestData[toFetchTestData]



def test_check_login():
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname)
    driver = web_driver()
    driver.fullscreen_window()
    username = ["NAME", "login[username]"]
    password = ["NAME", "login[password]"]
    SubmitBtn = ["ID", "send2"]
    mainmenu = ["CLASS_NAME", "ui.nav.items"]
    searchelem = ["ID", "search"]

    list = ["ID", "search_autocomplete"]
    listelem = ["TAG_NAME", "li"]
    elemname = ["By.CLASS_NAME", "qs-option-name"]

    loggingData.TEST_INFORMATION(namefile=functionname, message="*******Starting test - test_check_login********")
    TestData = readyaml(loggingData, toFetchTestData=inspect.currentframe().f_code.co_name)

    loggingData.TEST_INFORMATION(namefile=functionname, message="url - " + TestData['url'])
    driver.get(TestData['url'])

    assert TestData['url'], driver.current_url

    presence_of_element_located(loggingData, driver, functionname, username, timeout=5)

    username_textbox = find_element(driver, username)
    loggingData.TEST_INFORMATION(namefile=functionname, message="username - " + TestData['username'])
    username_textbox.send_keys(TestData['username'])

    loggingData.TEST_INFORMATION(namefile=functionname, message="password - " + TestData['password'])
    password_textbox = find_element(driver, password)
    password_textbox.send_keys(TestData['password'])

    SignIn_button = find_element(driver, SubmitBtn)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Press Submit Button")
    SignIn_button.submit()

    presence_of_element_located(loggingData, driver, functionname, mainmenu, timeout=10)
    actualUrl = driver.current_url
    expectedUrl = TestData['expected']
    loggingData.TEST_INFORMATION(namefile=functionname, message="expectedUrl - " + expectedUrl)
    loggingData.TEST_INFORMATION(namefile=functionname, message="actualUrl - " + actualUrl)
    assert expectedUrl, actualUrl
    loggingData.TEST_INFORMATION(namefile=functionname, message="*******End test - test_check_login********")

    search_element = find_element(driver, searchelem)
    search_element.send_keys("yoga")
    time.sleep(5)
    search_result = find_element(driver, list)
    #elementslist = search_result.find_elements(By.TAG_NAME, "li")
    elementslist = find_elements(search_result, listelem)
    for opt in elementslist:
        mytext = find_element(opt, elemname).text
        loggingData.TEST_INFORMATION(namefile=functionname, message=mytext)
    time.sleep(10)