# coding=utf-8
import unittest
import HTMLTestRunner
import coverage
import os

# 获取当前目录下的case目录
case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_case/netease')


def run_all():
    """匹配以哪个名字开头的文件"""
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="netease_test*.py", top_level_dir=None)
    print("查询到的测试用例为：", discover)
    return discover


if __name__ == '__main__':
    """生成代码使用率报告"""
    cov = coverage.Coverage()
    cov.start()
    filepath = 'Report\Report.html'
    file_result = open(filepath, 'wb')
    """生成测试报告"""
    runner = HTMLTestRunner.HTMLTestRunner(file_result, title='autotest_app test ', description='test report')
    runner.run(run_all())
    cov.stop()
    cov.save()
    cov.html_report()
    file_result.close()


