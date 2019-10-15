# coding = utf-8
import yaml


def test():
    file = open('Utils/config.yaml', 'rb')
    data = yaml.load(file)
    # 读取全部数据
    print(data)
    # 读取第一个platformVersion的值
    print(data["platformVersion"][0]["platformVersion"])


if __name__ == '__main__':
    test()
