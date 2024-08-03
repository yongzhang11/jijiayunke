# @Time：2024/8/3 8:21
# @Author: Allan
from DrissionPage import ChromiumPage, ChromiumOptions


class DrissionpageDriverConfig:
    def __init__(self):
        pass

    def driver_config(self):
        # co = ChromiumOptions()
        # # 最大化窗口
        # co.set_argument('--start-maximized')
        # co.headless()  # 无头模式
        page = ChromiumPage(timeout=10)
        return page
