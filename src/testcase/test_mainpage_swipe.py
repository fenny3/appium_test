# -*- coding: utf-8 -*-
"""
进入雪球首页，进入基金的新闻页（不是第一个基金按钮），对他以及它右侧的每个新闻栏目，执行上滑5次，进入下个栏目用从右边到左边滑动
滑动使用相对坐标，而不是绝对坐标
"""

import time
import logging

import allure
from appium.webdriver.webdriver import WebDriver

from src.common.driver import AppDriver
from config import config as Config

from src.uiconfig import main_page_ui as MainPageUI

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s %(asctime)s %(filename)s %(funcName)s line:%(lineno)d]: %(message)s',
                    datefmt='%y%m%d %H:%M:%S')

@allure.feature('测试主界面的滑动功能')
class TestMainPageSwipe:
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        cls.app_driver = AppDriver(Config.REMOTE_URL, Config.CAPS, Config.IMPLICITLY_WAIT_TIME)
        cls.driver = cls.app_driver.driver
        cls.win_size = cls.app_driver.window_size

    @allure.story('测试新闻栏目的滑动功能')
    @allure.title('测试基金及其之后每个新闻栏目的滑动功能')
    def test_1(self):
        self.driver.find_element_by_id(MainPageUI.xueqiu_button_id)
        with allure.step('进入基金栏目，并通过topic验证是否在基金栏目，然后上滑5次'):
            base_label_text = '基金'
            logging.info(MainPageUI.xueqiu_label_xpath.format(text=base_label_text))
            self.driver.find_element_by_xpath(MainPageUI.xueqiu_label_xpath.format(text=base_label_text)).click()
            self.driver.find_element_by_xpath(MainPageUI.xueqiu_jijin_topic_xpath.format(text=base_label_text))
            for i in range(5):
                self.app_driver.swipe('up')
                time.sleep(0.1)
        for i in range(20):
            logging.info(MainPageUI.xueqiu_label_by_brother_xpath.format(text=base_label_text))
            try:
                next_label = self.driver.find_element_by_xpath(MainPageUI.xueqiu_label_by_brother_xpath.format(text=base_label_text))
            except:
                logging.info('最后的新闻栏目为{}'.format(base_label_text))
                self.driver.save_screenshot(base_label_text + '.png')
                # with open(base_label_text + '.png', 'rb') as rbf:
                #     allure.attach('最后一个新闻栏目', rbf.read(), allure.attachment_type.PNG)
                # break
            base_label_text = next_label.text
            logging.info('进入{}栏目'.format(base_label_text))
            with allure.step('进入{0}栏目，并通过topic验证是否在{0}栏目，然后上滑5次'.format(base_label_text)):
                self.app_driver.swipe('left')
                self.driver.find_element_by_xpath(MainPageUI.xueqiu_jijin_topic_xpath.format(text=base_label_text))
                for i in range(5):
                    self.app_driver.swipe('up')
                    time.sleep(0.1)



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

