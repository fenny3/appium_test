# -*- coding: utf-8 -*-

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

class TestDemon:

    driver = WebDriver

    @classmethod
    def setup_class(cls):
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "demo",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noReset": True
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        cls.driver.implicitly_wait(10)
        cls.size = cls.driver.get_window_size()
        cls.width = cls.size['width']
        cls.height = cls.size['height']

    # def setup_method(self):
    #     pass

    # def test_login(self):
    #     TestDemon.driver.find_element_by_id("user_profile_icon").click()
    #     TestDemon.driver.find_element_by_id("tv_login").click()
    #     TestDemon.driver.find_element_by_id("tv_login_by_phone_or_others").click()

    def test_swipe(self):
        self.driver = TestDemon.driver
        TestDemon.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        for i in range(5):
            self.driver.swipe(800, 1000, 800, 200)
        self.driver.scroll()

    def test_scroll(self):
        action = TouchAction(self.driver)
        TestDemon.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        for i in range(15):
            action.press(x=TestDemon.width/2, y=TestDemon.height*3/4).move_to(x=TestDemon.width/2, y=TestDemon.height/4).release().perform()
            time.sleep(1)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

