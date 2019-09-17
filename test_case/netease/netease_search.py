import unittest
from Utils.appium_config import DriverClient
from Utils.action_config import action
from time import sleep


THINK_TIME = 3
class search_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @unittest.skip("do not test right now")
    def test_c_search(self):
        # click search button
        try:
            print("搜索按钮当前所处页面的活动名称为：%s" % self.driver.current_activity)
            # sleep(THINK_TIME)
            """make sure search button is show or not"""
            search = self.driver.find_element_by_accessibility_id("Search")
            flag = search.is_displayed()
            if flag:
                search.click()
                self.driver.wait_activity(".activity.SearchActivity", THINK_TIME)
                # locate search edit box
                sleep(THINK_TIME)
                edit = self.driver.find_element_by_id("com.netease.cloudmusic:id/search_src_text")
                item = "million years ago"
                edit.send_keys(item)
                # locate search button
                self.driver.find_element_by_id("com.netease.cloudmusic:id/c8e").click()
                sleep(THINK_TIME)
                """use swipe down method"""
                is_bottom = action().is_bottom()
                is_top = action().is_top()
                # self.driver.shake()
                self.assertEquals(True, is_bottom)
                self.assertEquals(True, is_top)
            else:
                pass
        except Exception as e:
            raise e





