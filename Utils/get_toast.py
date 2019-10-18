from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class get_toast():
    def get_toast(self, matchString, driver):
        toast_element = WebDriverWait(driver, 0.01). \
            until(EC.presence_of_element_located((By.XPATH, matchString)))
        return toast_element.text

    def element_is_present(self, driver, pattern):
        """
        :param driver:
        :param pattern: 查找元素使用的方法id,text等
        :return: boolean
        """
        el = WebDriverWait(driver, 1).until\
            (EC.presence_of_element_located(lambda x: By.x, pattern))
        print("输出获取到的元素的类型：", type(el))
        return el
