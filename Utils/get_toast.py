from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class get_toast():
    def get_toast(self, pattern, driver):
        """
        :param pattern: 需要匹配的xpath模板
        usage template: 使用示例
                message = "//*[contains(@text,'用户') or contains(@text,'成功')]"
                # 获取toast提示框内容
                toast_element = get_toast().get_toast(message, self.driver)
        :param driver: 驱动
        :return: webElement
        """
        try:
            toast_element = WebDriverWait(driver, 0.001). \
                until(EC.presence_of_element_located((By.XPATH, pattern)))
        except EC.NoAlertPresentException as e:
            print("未匹配到对应的语句！")
            raise e
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
