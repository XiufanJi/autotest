from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_toast(matchString, driver):
    toast_element = WebDriverWait(driver, 5). \
        until(EC.presence_of_element_located((By.XPATH, matchString)))
    return toast_element.text