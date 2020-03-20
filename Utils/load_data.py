# 加载文件内的内容进行显示使用，现在暂时不需要写方法来调用
import yaml


class load_data():
    def __init__(self, path, mode):
        """
        :param path: 文件路径
        :param mode: 文件读取模式
        """
        self.path = path
        self.mode = mode

    # 获取全部的数据
    def load_all_data(self):
        file = open(self.path, self.mode)
        data = yaml.safe_load(file)
        return data

    # 获取整个用例的个数
    def get_data_length(self):
        data = self.load_all_data()
        data_length = len(data["testcase"])
        # print("获取到的数据长度：{}".format(data_length))
        return data_length

    def get_desc(self, i):
        """
        :param i: 第几位的desc字段
        :return: desc
        """
        # print("第{0}位的描述词为{1}".format(i, self.load_all_data()["testcase"][i]["desc"]))
        return self.load_all_data()["testcase"][i]["desc"]

    def get_type(self, i):
        """
        :param i: 第几位的find_type字段
        :return: find_type
        """
        # print("第{0}位的find_type字段为{1}".format(i, self.load_all_data()["testcase"][i]["find_type"]))
        return self.load_all_data()["testcase"][i]["find_type"]

    def get_element_location(self, i):
        """
        :param i: 第几位的location字段
        :return: element_location
        """
        # print("第{0}位的location字段为{1}".format(i, self.load_all_data()["testcase"][i]["element_location"]))
        return self.load_all_data()["testcase"][i]["element_location"]

    def get_find_locator(self, i):
        """
        :param i: 第几位的locator字段
        :return: find_locator
        """
        # print("第{0}位的locator字段为{1}".format(i, self.load_all_data()["testcase"][i]["find_locator"]))
        return self.load_all_data()["testcase"][i]["find_locator"]

    def get_operate(self, i):
        """
        :param i: 第几位的operate字段
        :return: operate
        """
        # print("第{0}位的operate_1字段为{1}".format(i, self.load_all_data()["testcase"][i]["operate_1"]))
        return self.load_all_data()["testcase"][i]["operate"]

    def get_content(self, i):
        """
        :param i: 第几位的content字段
        :return: content
        """
        # print("第{0}位的content字段为{1}".format(i, self.load_all_data()["testcase"][i]["content"]))
        return self.load_all_data()["testcase"][i]["content"]

    def get_return(self, i):
        """
        :param i: 第几位的return字段
        :return: return
        """
        # print("第{0}位的return字段为{1}".format(i, self.load_all_data()["testcase"][i]["return_num"]))
        return self.load_all_data()["testcase"][i]["return_num"]

# load_data = load_data('../yaml/mobile/netease/login.yaml', 'rb').load_all_data()
# data_length = load_data('yamlFile/mobile/login.yaml', 'rb').get_data_length()

# data = load_data('yamlFile/mobile/login.yaml', 'rb').get_find_locator(0)
# print(load_data)

# print(data)