import os


class action():
    """判断APP是否已经安装，若未安装则进行安装"""
    def App_IsInstall(self, apk_name, apk_path):
        flag = os.system("adb shell pm list packages -3e | findstr {}".format(apk_name))
        print("apk检索结果：{}".format(flag))
        if flag != "":
            os.system("adb install -rt {}".format(apk_path))