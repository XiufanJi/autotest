from Utils.load_data import load_data as data
from time import sleep
from Utils.public_action import action
import os
# path = 'yaml/mobile/netease/login.yaml'
wait = 2


class operate_yaml():
    def __init__(self, path):
        self.data = data(path, 'rb')
        self.action = action()

    def operate_yaml(self, desc_match):
        data_length = self.data.get_data_length()
        if data_length != 0:
            for i in range(data_length):
                if self.data.get_operate_1(i) == 'click':
                    if self.data.get_find_locator(i) == 'normal':
                        """判断取到的数据是否符合自己的要求"""
                        if desc_match in self.data.get_desc(i):
                            """调用action类中的方法实现元素操作"""
                            self.action.find_element(self.data.get_type(i), self.data.get_element_location(i)).click()

                    elif self.data.get_find_locator(i) == 'android_uiautomator':
                        if desc_match in self.data.get_desc(i):
                            self.action.find_byUiautormator(self.data.get_type(i), self.data.get_element_location(i))\
                                .click()

                elif self.data.get_operate_1(i) == 'clear':
                    if self.data.get_operate_2(i) == 'send_keys':
                        if self.data.get_find_locator(i) == 'normal':
                            if desc_match in self.data.get_desc(i):
                                self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))\
                                    .clear()
                                sleep(wait)
                                self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))\
                                    .send_keys(self.data.get_content(i))
                        elif self.data.get_find_locator(i) == 'android_uiautomator':
                            if desc_match in self.data.get_desc(i):
                                self.action.find_byUiautormator(self.data.get_type(i)\
                                                                ,self.data.get_element_location(i)).clear()
                                sleep(wait)
                                self.action.find_byUiautormator(self.data.get_type(i)\
                                                                ,self.data.get_element_location(i)).\
                                    send_keys(self.data.get_content(i))
        else:
            return "yaml文件内数据为空！"


# test = operate_yaml().operate_yaml("同意")
# if __name__ == '__main__':
#     current = os.getcwd()
#     print(current)
