from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def presence_of_element_located(logging, driver, namefile, element, timeout):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        logging.TEST_INFORMATION(namefile=namefile, message="Timed out waiting for page to load")


def find_element(driver, element):
    return driver.find_element(*element)
