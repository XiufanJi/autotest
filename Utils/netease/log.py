import subprocess
import time


# not good to realize
class getLogCat():
    def getlogs(self):
        # 获取当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 日志文件名添加当前时间
        filename = "./Log/" + now + r"_log.txt"
        logcat_file = open(filename, 'w')
        logcmd = "adb logcat -v time --I"
        poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        logcat_file.close()
        poplog.terminate()