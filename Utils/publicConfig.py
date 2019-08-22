from appium import webdriver

accountRegx = "((^(13|14|15|16|17|18|19)\d{9}$))"
passregx = "(^\w{6,18}$)"
idregx = "(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)"
num=""

class Singleton():
    driver=None
    def driverConfig(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "192.168.251.101:5555",
            "platformVersion": "8.0.0",
            "automationName": "UiAutomator2",
            "appPackage": "com.conlin360.medical",
            "appActivity": "com.conlin360.medical.activity.mine.SplashActivity"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return self.driver

class driverClient(Singleton):
    def getDriver(self):
        return self.driver
