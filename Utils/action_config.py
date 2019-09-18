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
        start_x = action().get_window_size()[0]/2
        start_y = action().get_window_size()[1]*3/4
        end_x = action().get_window_size()[0]/2
        end_y = action().get_window_size()[1]/4
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        return start_x, start_y, end_x, end_y

    """针对页面的上滑操作"""
    def swipe_up(self):
        start_x = action().get_window_size()[0]*3/4
        start_y = action().get_window_size()[1]/5
        end_x = action().get_window_size()[0]*3/4
        end_y = action().get_window_size()[1]*2/5
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
        return start_x, start_y, end_x, end_y

    """针对特定区域无法单独对元素进行定位但是可以对整块区域进行定位的左右滑动操作"""
    def swipe_right(self, start_x, end_x, y):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        usage like:
        start_x, y, end_x, y = width / 3, height / 2, width *2/ 3, height / 2
        右滑需要start_x的值小于end_x的值：较小值朝较大值滑去
        :return:end_x
        """
        sleep(THINK_TIME)
        self.driver.swipe(start_x, y,
                          end_x, y, 200)
        return end_x

    """针对特定区域无法单独对元素进行定位的左右滑动操作"""
    def swipe_left(self, start_x, end_x, y):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        :return:end_x
        usage: 左滑需要start_x的坐标值大于end_x的值，较大值朝较小值滑去
        """
        self.driver.swipe(start_x, y, end_x, y, 200)
        return end_x

    """针对需要滑动的目标不能进行区域定位，但是可以进行单独定位的情况"""
    def element_scroll(self, origin_el, destination_el):
        """
        :param origin_el: 起始元素
        :param destination_el: 终止元素
        :return:
        """
        self.driver.scroll(origin_el, destination_el, 200)

    """判断是否滑动到页面底部：上滑和下滑适用"""
    def top_bottom(self, direction):
        sleep(THINK_TIME)
        # driver.shake()方法现在只支持iOS使用，Android暂不支持
        # self.driver.shake()
        screen_height = action().get_window_size()[1]
        flag, count, is_bottom, temp = True, 0, False, 0
        while flag:
            if direction == "down":
                action().swipe_down()
                height = action().swipe_down()[3]
            else:
                action().swipe_up()
                height = action().swipe_up()[3]
            count += 1
            temp += height
            print("第{0}次{1}滑动后的高度值：{2:.2f}".format(count, direction, temp))
            if temp >= screen_height:
                flag = False
                is_bottom = True
        print("屏幕的高度：%d" % screen_height)
        print("滑动是否到达页面底部：%s" % is_bottom)
        return is_bottom

    # 判断左/右滑是否滑动到页面边缘
    def left_right(self, start_x, end_x, y,direction):
        """
        :param start_x: 滑动起始点的x轴位置，根据获取到的区域总宽度来确定x的取值比
        :param end_x: 滑动过程中的x轴的变化量
        :param y: 滑动的区域的y轴位置，因左右滑动时，y值无变化，所以可取同一值
        :return: boolean:is_left
        """
        flag, count, is_border, totalscroll = True, 0, False, 0
        screen_width = action().get_window_size()[0]
        while flag:
            if direction == "right":
                action().swipe_right(start_x, end_x, y)
                scroll_width = action().swipe_right(start_x, end_x, y)
            else:
                action().swipe_left(start_x, end_x, y)
                scroll_width = action().swipe_left(start_x, end_x, y)
            count += 1
            totalscroll += scroll_width
            print("第{0}次{1}滑动后的宽度值：{2:.2f}".format(count, direction, totalscroll))
            if totalscroll >= screen_width:
                flag = False
                is_border = True
        print("屏幕的宽度：%d" % screen_width)
        print("滑动是否到达页面顶部：%s" % is_border)
        return is_border

    # el = self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true))."
    #                                                      "scrollIntoView(new UiSelector().text(\"听听\"))")

