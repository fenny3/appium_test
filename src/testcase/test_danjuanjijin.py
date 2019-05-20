# -*- coding: utf-8 -*-
"""
基金开户 蛋卷已有账户登录 密码登陆 输入错误的用户名和密码，点击安全登陆
"""
import time
import pytest
import allure
from appium.webdriver.webdriver import WebDriver

from src.common.driver import AppDriver
from config import config as Config
from src.uiconfig import jiaoyi_tab as JiaoYiUI

@allure.feature('基金开户')
class TestDanJuanJiJin:
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        cls.app_driver = AppDriver(Config.REMOTE_URL, Config.CAPS, Config.IMPLICITLY_WAIT_TIME)
        cls.driver = cls.app_driver.driver

    def setup_method(self):
        self.driver.find_element_by_xpath('//*[contains(@text, "赞")]')
        self.driver.find_element_by_xpath('//*[@text="交易" and @resource-id="com.xueqiu.android:id/tab_name"]').click()

    @allure.story('测试蛋卷已有账户登录')
    @allure.title('密码登录，输入错误的用户名和密码')
    @pytest.mark.parametrize('account, passwd', [('13800000000', '123456')])
    def test_danjuan(self,account, passwd):
        with allure.step('点击基金开户条目，进入蛋卷基金页面'):
            self.driver.find_element_by_xpath(JiaoYiUI.label_xpath.format('基金开户')).click()
        with allure.step('选择蛋卷已有账户登录'):
            self.driver.find_element_by_xpath(JiaoYiUI.label_xpath.format('已有蛋卷基金账户登录')).click()
        with allure.step('密码登录，输入错误的用户名和密码'):
            self.driver.find_element_by_xpath(JiaoYiUI.label_xpath.format('使用密码登录')).click()
            self.driver.find_element_by_xpath(JiaoYiUI.label_xpath.format('使用验证码登录'))

            # ###xpath 适用于uiautomator2 及 默认的方式
            self.driver.find_element_by_xpath(JiaoYiUI.login_xpath.format('telno')).send_keys(account)
            self.driver.find_element_by_xpath(JiaoYiUI.login_xpath.format('pass')).send_keys(passwd)
            self.driver.find_element_by_xpath(JiaoYiUI.login_xpath.format('next')).click()

            ##by id 适用于appium默认的
            # self.driver.find_element_by_id('telno').send_keys(account)
            # self.driver.find_element_by_id('pass').send_keys(passwd)
            # self.driver.find_element_by_id('next').click()

        with allure.step('验证错误的用户名密码登录给出失败的提示'):
            message = self.driver.find_element_by_xpath(JiaoYiUI.login_xpath.format('android:id/message')).get_attribute('text')
            assert message == '你输入的手机号码或者密码有误'
            self.driver.find_element_by_xpath(JiaoYiUI.login_xpath.format('android:id/button1')).click()

    # def teardown_method(self):
    #     self.driver.back()
    #     self.driver.back()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



