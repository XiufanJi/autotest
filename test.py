# coding = utf-8
import yaml
import os
import unittest


def test():
    # file = open('Utils/config.yaml', 'rb')
    # data = yaml.load(file)
    # # 读取全部数据
    # print(data)
    # # 读取第一个platformVersion的值
    # print(data["platformVersion"][0]["platformVersion"])
    chrome_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'base')
    print("chrome", chrome_dir)
    # discover = unittest.defaultTestLoader.discover(chrome_dir, pattern="chrome_*.exe", top_level_dir=None)
    # print(discover)



if __name__ == '__main__':
    test()
