from Utils.appium_config import DriverClient
from time import sleep


THINK_TIME = 2
class window_action():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    def get_window_size(self):
        window = self.driver.get_window_size("current")
        self.driver.get_window_rect()
        x = window["width"]
        y = window["height"]
        # print(type(window))
        # 将字典以字符串类型输出
        # print(str(window))
        # print(x,y)
        return x, y

    def swipe_down(self):
        """start_x,start_y：滑动的起始点,end_x,end_y:每次滑动的跨度，并不是滑动的终点值"""
        start_x = window_action().get_window_size()[0] / 2
        start_y = window_action().get_window_size()[1] * 3 / 4
        end_x = window_action().get_window_size()[0] / 2
        end_y = window_action().get_window_size()[1] / 10
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        return start_x, start_y, end_x, end_y

    def is_bottom(self):
        sleep(THINK_TIME)
        # check if user button is show
        # self.driver.shake()
        screen_height = window_action().get_window_size()[1]
        height = window_action().swipe_down()[3]
        flag, count = True, 0
        while flag:
            window_action().swipe_down()
            # user = self.driver.find_element_by_id("com.netease.cloudmusic:id/c8b").is_displayed()
            count += 1
            height += height
            if height >= screen_height:
                flag = False
            print("第{0}次滑动后的高度值：{1}".format(count, height))
        print("屏幕的高度：%d" % screen_height)
        print("滑动是否到达页面底部：%s" % flag)
        return flag



# if __name__ == '__main__':
#     size = window_action()
#     windowsize = size.get_window_size()

