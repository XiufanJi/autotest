from appium import webdriver
# from Test.logs.logs import logging  # 本人自己封装的方法，你们写时可以不用调用，并且删除方法中调用的logging即可
import yaml
import os


# test = "D:\BaiduNetdiskDownload\chromedriver_win32_66\chromedriver.exe"
"""调试文件读取路径"""
test = '../../../yaml/preConfig.yaml'
"""配置文件的读取路径"""
path = 'd://autoTest/yaml/preConfig.yaml'
cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  #获取当前项目的根路径
app = cur_path+"\\app\\jiankanglanxi.apk"

"""文件路径的确是大问题：之前测试的时候写的是相对路径，结果过了一个月之后，居然不行了，单独测试的时候是可以打印数据的，
结果整个结合用例跑的时候就是无法启动appium，得好好研究下，写一个好的方法来实现"""


class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            # logging.info('-----------------------init driver----------------------')
            """从配置文件中读取相应的配置项"""
            # file = open(test, 'rb')
            file = open(path, 'rb')
            data = yaml.load(file)
            # appPackage = apk_path+"/app/"+data["app"][0]["appPackage"]
            config = {
                "deviceName": data["device"][4]["deviceName"],
                "platformVersion": data["platformVersion"][1]["platformVersion"],
                "platformName": data["platformName"],
                "automationName": data["autormator"][1]["automationName"],
                "appPackage": data["app"][0]["appPackage"],
                "appActivity": data["appActivity"][0]["appActivity"],
                # 切换小程序时使用
                # "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"},
                "noReset": "true",
                "fullReset": "false"
                # 指定chromeDriver的执行路径，chromedriver单独放置时使用,切换webview页面时使用
                # "chromedriverExecutable": data["chromeDriver"][0]["chromeDriver"]
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)
        return cls._instance


class DriverClient(Singleton):
    def getDriver(self):
        # logging.info('get driver')
        return self.driver


# if __name__ == '__main__':
#     current = os.getcwd()
#     flag = os.path.exists(preConfig)
#     print(flag, current)