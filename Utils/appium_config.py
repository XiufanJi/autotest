from appium import webdriver
# from Test.logs.logs import logging  # 本人自己封装的方法，你们写时可以不用调用，并且删除方法中调用的logging即可


class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            # logging.info('-----------------------init driver----------------------')
            config = {
                # conlin app config
                # system:android 8.0
                # "platformName": "Android",
                # "deviceName": "192.168.251.101:5555",
                # "platformVersion": "8.0.0",
                # "automationName": "UiAutomator2",
                # "appPackage": "com.conlin360.medical",
                # "appActivity": "com.conlin360.medical.activity.mine.SplashActivity"
                # netease app config
                "deviceName": "f0dc688e",
                "platformVersion": "4.4.4",
                # """使用真机调试"""
                "platformName": "Android",
                # "deviceName": "a8a5e0d07cf4",
                # "plateforVersion": "7.1.2",
                """获取toast，使用UIAutomator2"""
                "automationName": "UIAutomator1",
                # "appPackage": "com.netease.cloudmusic",
                # "appActivity": "com.netease.cloudmusic.activity.LoadingActivity"
                # "appPackage": "com.autonavi.minimap",
                # "appActivity": "com.autonavi.map.activity.SplashActivity"
                # "appPackage": "com.baidu.BaiduMap",
                # "appActivity": "com.baidu.baidumaps.guide.TermsActivity"
                "appPackage": "com.tencent.map",
                "appActivity": "com.tencent.map.WelcomeActivity"
                # 'autoLaunch':'false'   #appium是否要自动启动或安装APP，默认为ture
                # 'newCommandTimeout':'60'  #设置未接受到新命令的超时时间，默认60s，说明：如果60s内没有接收到新命令，
                # appium会自动断开，
                #如果我需要很长时间做driver之外的操作，可设置延长接收新命令的超时时间
                # 'unicodeKeyboard':True,
                # 'resetKeyboard':True
                # 'noReset':'false'  #在会话前是否重置APP状态，默认是false
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)
        return cls._instance


class DriverClient(Singleton):

    def getDriver(self):
        # logging.info('get driver')
        return self.driver