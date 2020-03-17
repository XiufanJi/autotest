# coding = utf-8
import re


def test():
    pattern = "^[A-Za-z]+|[\u4e00-\u9fa5]+$"
    sentence = "你好"
    flag = re.findall(pattern, sentence)
    print(type(flag))
    print(flag)


if __name__ == '__main__':
    test()
