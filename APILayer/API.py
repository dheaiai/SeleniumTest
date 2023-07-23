from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def by_locator(byclass):
    if byclass == "NAME":
        return By.NAME
    elif byclass == "ID":
        return By.ID
    elif byclass == "CLASS_NAME":
        return By.CLASS_NAME
    elif byclass == "XPATH":
        return By.XPATH
    elif byclass == "TAG_NAME":
        return By.TAG_NAME


def presence_of_element_located(logging, driver, namefile, element, timeout):
    try:
        element_present = EC.presence_of_element_located((by_locator(element[0]), element[1]))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        logging.TEST_INFORMATION(namefile=namefile, message="Timed out waiting for page to load")


def find_element(driver, element):
    return driver.find_element(by_locator(element[0]), element[1])


def find_elements(driver, element):
    return driver.find_elements(by_locator(element[0]), element[1])


def web_driver():
    return webdriver.Chrome()
