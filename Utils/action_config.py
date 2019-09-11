from Utils.appium_config import DriverClient


class window_action():
    def __init__(self):
        self.driver = DriverClient().getDriver()

    def get_window_size(self):
        window = self.driver.get_window_size("current")
        x = window["width"]
        y = window["height"]
        # print(type(window))
        # print(x,y)
        return x, y

    def swipe_up(self):
        start_x = window_action().get_window_size()[0]
        start_y = window_action().get_window_size()[1]
        end_x = window_action().get_window_size()[0]
        end_y = window_action().get_window_size()[1]
        self.driver.swipe(-start_x, -start_y, end_x, end_y, 2000)
# if __name__ == '__main__':
#     size = get_size()
#     windowsize = size.get_window_size()

