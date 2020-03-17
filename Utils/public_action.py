import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class pub_action():
    """判断APP是否已经安装，若未安装则进行安装"""
    def App_IsInstall(self, apk_name, apk_path):
        flag = os.system("adb shell pm list packages -3e | findstr {}".format(apk_name))
        """返回的结果，若检索到相关的安装包，则会返回0，若未检索到安装包，则返回1（很好奇为什么不是返回布尔类型，
        而是int,因为只有0和1两个值）"""
        # print(type(flag))
        if flag == 1:
            print("{0}安装包是否安装的检索结果：{1}".format(apk_name, "未安装"))
            os.system("adb install -rt {}".format(apk_path))
        else:
            print("{0}安装包是否安装的检索结果：{1}".format(apk_name, "已安装"))

    """获取文件的相对路径"""
    def get_path(self, file_path):
        """
        :param file_path: 需要访问的文件，如：yaml/mobile/lanxi/login.yaml
        :return: rel_path:所需访问文件的相对路径
        """
        dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        rel_path = os.path.relpath(os.path.join(dir_path, file_path))
        return rel_path

    """获取页面上弹出的toast信息"""
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

    """判断元素是否出现在页面上"""
    def element_is_present(self, driver, locator, pattern):
        """
        :param driver: 使用的驱动
        :param locator: 定位的方式，id,classname ...
        :param pattern: 需要进行匹配的字段
        :return: web element
        """
        el = WebDriverWait(driver, 1).until\
            (EC.presence_of_element_located(By.locator, pattern))
        print("输出获取到的元素的类型：", type(el))
        return el


# if __name__ == '__main__':
#     action = action()
#     rel = action.get_path("yaml\\mobile\\lanxi\\login.yaml")
#     print(rel)
#     print(os.getcwd())