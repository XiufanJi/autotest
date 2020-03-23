from Utils.load_data import load_data as data
from Utils.appium_action import action
# from Utils.public_action import pub_action
# file_path = pub_action().get_path("yaml/mobile/lanxi/patient.yaml")


class operate_yaml():
    def __init__(self, path):
        self.data = data(path, 'rb')
        self.action = action()

    def operate_yaml(self, desc_match):
        """
        :param desc_match: 元素的描述，对应yaml的desc字段
        :return: tuple('element','content')
        """
        el = None
        content = ""
        data_length = self.data.get_data_length()
        if data_length != 0:
            for i in range(data_length):
                """判断取到的数据是否符合自己的要求"""
                if desc_match == self.data.get_desc(i):
                    if self.data.get_find_locator(i) == 'normal':
                        """调用action类中的方法实现元素操作"""
                        if self.data.get_return(i) == "single":
                            if self.data.get_operate(i) == "send_keys":
                                el = self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))
                                content = self.data.get_content(i)
                            else:
                                el = self.action.find_element(self.data.get_type(i), self.data.get_element_location(i))
                        elif self.data.get_return(i) == "more":
                            el = self.action.find_elements(self.data.get_type(i), self.data.get_element_location(i))

                    elif self.data.get_find_locator(i) == 'android_uiautomator':
                        if self.data.get_return(i) == "single":
                            if self.data.get_operate(i) == "send_keys":
                                el = self.action.find_byUiautormator(self.data.get_type(i), \
                                                                     self.data.get_element_location(i))
                                content = self.data.get_content(i)
                            else:
                                el = self.action.find_byUiautormator(self.data.get_type(i), \
                                                                     self.data.get_element_location(i))
                        elif self.data.get_return(i) == "more":
                            el = self.action.find_elements_byUiautormator(self.data.get_type(i), \
                                                                          self.data.get_element_location(i))
                # else:
                #     print("输入的元素描述与获取到的数据不一致")
            return el, content
        else:
            return "yaml文件内数据为空！"


# if __name__ == '__main__':
#     data = operate_yaml(file_path).operate_yaml("请输入姓名")
#     print(type(data))
#     print(data[1])

