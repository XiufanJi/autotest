from Utils.appium_config import DriverClient
from time import sleep


THINK_TIME = 2
class action():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    """获取页面长宽"""
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

    """针对页面的下滑操作"""
    def swipe_down(self):
        """start_x,start_y：滑动的起始点,end_x,end_y:每次滑动的跨度，并不是滑动的终点值
            若是需要自行设置相应的起始点以及滑动的移动量大小，则可将下面的数据都作为参数传入
        """
        start_x = action().get_window_size()[0] / 2
        start_y = action().get_window_size()[1] * 3 / 4
        end_x = action().get_window_size()[0] / 2
        end_y = action().get_window_size()[1] / 10
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        return start_x, start_y, end_x, end_y

    def swipe_up(self):
        start_x = action().get_window_size()[0]*3/4
        start_y = action().get_window_size()[1] / 5
        end_x = action().get_window_size()[0]*3/4
        end_y = action().get_window_size()[1]*4 / 10
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        return start_x, start_y, end_x, end_y

    def swipe_right(self, start_x, end_x, y):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        usage like:
        start_x, y, end_x, y = width / 2, height / 2, width / 4, height / 2
        :return:end_x
        """
        sleep(THINK_TIME)
        self.driver.swipe(start_x, y,
                          end_x, y, 200)
        return end_x

    def swipe_left(self,start_x,end_x,y):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        :return:end_x
        """
        self.driver.swipe(start_x,y,end_x,y,200)
        return end_x




    """判断是否滑动到页面底部"""
    def is_bottom(self):
        sleep(THINK_TIME)
        # driver.shake()方法现在只支持iOS使用，Android暂不支持
        # self.driver.shake()
        screen_height = action().get_window_size()[1]
        height = action().swipe_down()[3]
        flag, count, is_bottom = True, 0, False
        while flag:
            action().swipe_down()
            count += 1
            height += height
            print("第{0}次滑动后的高度值：{1}".format(count, height))
            if height >= screen_height:
                flag = False
                is_bottom = True
        print("屏幕的高度：%d" % screen_height)
        print("滑动是否到达页面底部：%s" % is_bottom)
        return is_bottom


    """判断是否滑动到页面顶部：现在判断还是有点问题:因为每次滑动的距离好像并不等于设置的值"""
    def is_top(self):
        flag, count, is_top = True, 0, False
        window_height = action().get_window_size()[1]
        while flag:
            action().swipe_up()
            count += 1
            height = action().swipe_up()[3]
            window_height = window_height-height
            print("第{0}次滑动后的高度值：{1:.2f}".format(count, window_height))
            if window_height <= 0:
                flag = False
                is_top = True
        # print("屏幕的高度：%d" % screen_height)
        print("滑动是否到达页面顶部：%s" % is_top)
        return is_top

    # 判断右滑是否滑动到页面边缘
    def is_right(self, start_x, end_x, y):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        :return: boolean:is_left
        """
        flag, count, is_right, totalscroll = True, 0, False, 0
        window_width = action().get_window_size()[0]
        while flag:
            action().swipe_right(start_x, end_x, y)
            count += 1
            scroll_width = action().swipe_right(start_x, end_x, y)
            totalscroll += scroll_width
            print("第{0}次滑动后的宽度值：{1:.2f}".format(count, totalscroll))
            if totalscroll >= window_width:
                flag = False
                is_right = True
        # print("屏幕的高度：%d" % screen_height)
        print("滑动是否到达页面顶部：%s" % is_right)
        return is_right




# if __name__ == '__main__':
#     size = action()
#     windowsize = size.get_window_size()

