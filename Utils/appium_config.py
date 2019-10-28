from appium import webdriver
# from Test.logs.logs import logging  # 本人自己封装的方法，你们写时可以不用调用，并且删除方法中调用的logging即可
import yaml


# test = "D:\BaiduNetdiskDownload\chromedriver_win32_66\chromedriver.exe"
class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            # logging.info('-----------------------init driver----------------------')
            """从配置文件中读取相应的配置项"""
            file = open('Utils/yamlFile/preConfig.yaml', 'rb')
            data = yaml.load(file)
            config = {
                "deviceName": data["device"][2]["deviceName"],
                "platformVersion": data["platformVersion"][5]["platformVersion"],
                "platformName": data["platformName"],
                "automationName": data["autormator"][1]["automationName"],
                "appPackage": data["app"][0]["appPackage"],
                "appActivity": data["appActivity"][0]["appActivity"],
                # "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"},
                "noReset": "true",
                "fullReset": "false"
                # 指定chromeDriver的执行路径，chromedriver单独放置时使用
                # "chromedriverExecutable": data["chromeDriver"][0]["chromeDriver"]
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)
        return cls._instance


class DriverClient(Singleton):

    def getDriver(self):
        # logging.info('get driver')
        return self.driver