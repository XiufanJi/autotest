# coding=utf-8
import unittest
import HTMLTestRunner
import coverage
import os
from Utils.appium_config import DriverClient

# case_path = os.path.join(os.getcwd(), ".")
case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.') #获取当前目录下的case目录

def run_all():
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*.py", top_level_dir=None)
    print("查询到的测试用例为：", discover)
    return discover

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    filepath = '..\Report\Result.html'
    file_result = open(filepath, 'wb')
    # discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)
    # print("查询到的测试用例为：", discover)
    runner = HTMLTestRunner.HTMLTestRunner(file_result, title='autotest_app test ', description='test report')
    runner.run(run_all())
    cov.stop()
    cov.save()
    cov.html_report()
    file_result.close()

