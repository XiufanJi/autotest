import unittest
from Utils.appium_config import DriverClient
from Utils.action_config import window_action
from time import sleep


THINK_TIME = 3
class search_music(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverClient().getDriver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_c_search(self):
        # click search button
        try:
            search = self.driver.find_element_by_accessibility_id("Search")
            flag = search.is_displayed()
            if flag:
                search.click()
                self.driver.wait_activity(".activity.SearchActivity", THINK_TIME)
                # locate search edit box
                sleep(THINK_TIME)
                edit = self.driver.find_element_by_id("com.netease.cloudmusic:id/search_src_text")
                item = "a million years ago"
                edit.send_keys(item)
                # locate search button
                self.driver.find_element_by_id("com.netease.cloudmusic:id/c8e").click()
                sleep(THINK_TIME)
                window_action().swipe_up()
            else:
                pass
        except Exception as e:
            raise e





