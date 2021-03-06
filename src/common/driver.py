# -*- coding: utf-8 -*-
"""
创建driver
"""
import time
import subprocess

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config import config as Config


class AppDriver:

    def __init__(self,remote_url: str, caps: dict, wait_time: int) -> None:
        self.wait_time = wait_time
        self.driver = webdriver.Remote(remote_url, caps)
        self.driver.implicitly_wait(self.wait_time)
        self.window_size = self.driver.get_window_size()
        self.width = self.window_size['width']
        self.height = self.window_size['height']
        self.prefix = "find_element_by"

    def swipe(self, direction: str='up', duration: int=0) -> None:
        if direction == 'up':
            self.driver.swipe(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, duration)
        elif direction == 'down':
            self.driver.swipe(self.width / 2, self.height / 4, self.width / 2, self.height * 3 / 4, duration)
        elif direction == 'right':
            self.driver.swipe(self.width / 8, self.height / 2, self.width * 7 / 8, self.height / 2, duration)
        elif direction == 'left':
            self.driver.swipe(self.width * 7 / 8, self.height / 2, self.width / 8, self.height / 2, duration)
        else:
            raise Exception('!!!滑动方向填写错误!!!')

    def click(self, by: str, value: str) -> None:
        function_name = self.prefix + "_" + by
        real_function_name = getattr(self.driver, function_name)
        real_function_name(value).click()

    def wait_element_displayed(self, by: str, value: str, wait: int=10, message: str='') -> WebElement or bool:
        function_name = self.prefix + "_" + by
        real_function_name = getattr(self.driver, function_name)
        max_time = time.time() + wait
        while time.time() < max_time:
            try:
                return real_function_name(value)
            except WebDriverException:
                pass
            time.sleep(0.2)
        raise NoSuchElementException(message)


    def whether_element_displayed(self, by: str, value: str, wait: int=10, message: str='') -> WebElement or bool:
        function_name = self.prefix + "_" + by
        real_function_name = getattr(self.driver, function_name)
        max_time = time.time() + wait
        try:
            while time.time() < max_time:
                try:
                    return real_function_name(value)
                except WebDriverException:
                    pass
                time.sleep(0.2)
            raise NoSuchElementException(message)
        except:
            return False

    def wait_element_present1(self, by: str, value: str, wait: int=10, fre: float=0.5) -> WebElement:
        function_name = self.prefix + '_' + by
        element = WebDriverWait(self.driver, wait, poll_frequency=fre, ).until(lambda x: getattr(x, function_name)(value))
        print(element)
        return element

    def wait_element_present2(self, by: str, value: str, wait: int=10, fre: float=0.5) -> WebElement:
        # by_str = MobileBy.XPATH
        if by == 'xpath':
            by_str = MobileBy.XPATH
        elif by == 'accessibility_id':
            by_str = MobileBy.ACCESSIBILITY_ID
        elif by == 'class_name':
            by_str = MobileBy.CLASS_NAME
        else:
            raise Exception('by is error')
        element = WebDriverWait(self.driver, wait, poll_frequency=fre
                                ).until(EC.presence_of_element_located
                                                          ((by_str, value)))
        print(element)
        return element


    def restart_app(self):
        cmd = "adb shell am start -W -S {package}/{activity}".format(package=Config.CAPS['appPackage'],activity=Config.CAPS['appActivity'])
        subprocess.call(cmd, shell=True)

