# coding=utf-8
import unittest
import HTMLTestRunner
import coverage
import os
from time import sleep
from Utils.public_action import pub_action

# 获取当前目录下的case目录
case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_case/lanxi/mine')
"""获取需要安装的apk目录"""
apk_dir = pub_action().get_path("app/com.conlin360.medical.apk")


def run_all():
    """匹配以哪个名字开头的测试用例文件"""
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*.py", top_level_dir=None)
    # print("查询到的测试用例为：", discover)
    return discover


if __name__ == '__main__':
    """生成代码使用率报告"""
    cov = coverage.Coverage()
    cov.start()
    """开始运行用例之前先进行apk安装检测"""
    pub_action().App_IsInstall("com.conlin360.medical", apk_dir)
    sleep(3)
    """代码使用率报告保存文件夹"""
    filepath = 'report\Report.html'
    file_result = open(filepath, 'wb')
    """生成测试报告，失败后重跑一次"""
    runner = HTMLTestRunner.HTMLTestRunner(file_result, title='autotest_app test ', description='test report', retry=1)
    runner.run(run_all())
    cov.stop()
    cov.save()
    cov.html_report()
    file_result.close()


