from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class get_toast():
    def get_toast(self, matchString, driver):
        toast_element = WebDriverWait(driver, 0.001). \
            until(EC.presence_of_element_located((By.XPATH, matchString)))
        return toast_element.text

    def element_is_present(self, driver, locator, pattern):
        """
        :param driver: 使用的驱动
        :param x: 定位的方式，id,classname ...
        :param pattern:
        :return: web element
        """
        el = WebDriverWait(driver, 1).until\
            (EC.presence_of_element_located(By.locator, pattern))
        print("输出获取到的元素的类型：", type(el))
        return el
