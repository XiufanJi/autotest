from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class get_toast():
    def get_toast(matchString, driver):
        toast_element = WebDriverWait(driver, 0.01). \
            until(EC.presence_of_element_located((By.XPATH, matchString)))
        return toast_element.text

    def element_is_present(self, driver, pattern):
        """
        :param driver:
        :param pattern: 查找元素使用的方法id,text等
        :return: boolean
        """
        el = WebDriverWait(driver, 2).until\
            (EC.presence_of_element_located(lambda x: driver.find_element_by_x(pattern).is_displayed()))
        if el:
            return True
        else:
            return False