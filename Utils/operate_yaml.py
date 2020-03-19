from Utils.load_data import load_data as data
from time import sleep
from Utils.appium_action import action
# from Utils.public_action import pub_action
# file_path = pub_action().get_path("yaml/mobile/lanxi/patient.yaml")


wait = 2


class operate_yaml():
    def __init__(self, path):
        self.data = data(path, 'rb')
        self.action = action()

    def operate_yaml(self, desc_match):
        """
        :param desc_match: 元素的描述，对应yaml的desc字段
        :return: webElement/webElements
        """
        data_length = self.data.get_data_length()
        if data_length != 0:
            for i in range(data_length):
                """判断取到的数据是否符合自己的要求"""
                if desc_match == self.data.get_desc(i):
                    if self.data.get_operate_1(i) == 'click':
                        if self.data.get_find_locator(i) == 'normal':
                            """调用action类中的方法实现元素操作"""
                            self.action.find_element(self.data.get_type(i), self.data.get_element_location(i)).click()

                        elif self.data.get_find_locator(i) == 'android_uiautomator':
                            if desc_match == self.data.get_desc(i):
                                self.action.find_byUiautormator(self.data.get_type(i),\
                                                                self.data.get_element_location(i)).click()

                    elif self.data.get_operate_1(i) == 'clear':
                        if self.data.get_operate_2(i) == 'send_keys':
                            if self.data.get_find_locator(i) == 'normal':
                                self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))\
                                    .clear()
                                sleep(wait)
                                self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))\
                                    .send_keys(self.data.get_content(i))
                            elif self.data.get_find_locator(i) == 'android_uiautomator':
                                self.action.find_byUiautormator(self.data.get_type(i)\
                                                                ,self.data.get_element_location(i)).clear()
                                sleep(wait)
                                self.action.find_byUiautormator(self.data.get_type(i)\
                                                                ,self.data.get_element_location(i)).\
                                    send_keys(self.data.get_content(i))

                    elif self.data.get_operate_1(i) == 'None':
                        print("获取到的描述为:"+self.data.get_desc(i))
                        print("输入的描述词:"+desc_match)
                        flag = desc_match == self.data.get_desc(i)
                        print("是否相等：{}".format(flag))
                        if self.data.get_find_locator(i) == "normal":
                            if self.data.get_return(i) == "single":
                                self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))
                            elif self.data.get_return(i) == "more":
                                self.action.find_elements(self.data.get_type(i), self.data.get_element_location(i))
                        elif self.data.get_find_locator(i) == 'android_uiautomator':
                            if self.data.get_return(i) == "single":
                                self.action.find_byUiautormator(self.data.get_type(i),\
                                                                self.data.get_element_location(i))
                            elif self.data.get_return(i) == "more":
                                self.action.find_elements_byUiautormator(self.data.get_type(i), \
                                                                self.data.get_element_location(i))
                else:
                    print("输入的元素描述与获取到的数据不一致")
        else:
            return "yaml文件内数据为空！"


# if __name__ == '__main__':
#     operate_yaml(file_path).operate_yaml("证件号码")
