#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
测试功能：打开雪球 添加自选股 输入alibaba 添加到自选股
"""

from selenium.common.exceptions import WebDriverException
from appium import webdriver

IMPLICITLY_WAIT_TIME = 10


def whether_element_displayed(appium_driver, strategy, value, wait_time=10):
    prefix = "find_element_by"
    function_name = prefix + "_" + strategy
    real_function_name = getattr(appium_driver, function_name)
    print(real_function_name)
    appium_driver.implicitly_wait(wait_time)
    try:
        try:
            return real_function_name(value)
        except WebDriverException:
            return False
    finally:
        appium_driver.implicitly_wait(IMPLICITLY_WAIT_TIME)


def test_xueqiu(appium_driver):
    size = appium_driver.get_window_size()
    print(size)
    appium_driver.find_element_by_id("com.xueqiu.android:id/quick_action").click()
    appium_driver.find_element_by_id("com.xueqiu.android:id/item_add_stock").click()
    search_input = appium_driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    search_input.send_keys("alibaba")
    appium_driver.find_element_by_xpath(
        ".//android.widget.TextView[@text='BABA']/../../following-sibling::android.widget.LinearLayout").click()

    # 判断是否有评论对话框
    dialog = whether_element_displayed(appium_driver, "id", "com.xueqiu.android:id/md_buttonDefaultNegative")
    if dialog:
        dialog.click()

    # 验证按钮变为已添加状态
    appium_driver.find_element_by_xpath(
        ".//android.widget.TextView[@text='BABA']/../../following-sibling::android.widget.LinearLayout/android.widget.TextView[@resource-id='com.xueqiu.android:id/followed_btn']")
    appium_driver.find_element_by_id("com.xueqiu.android:id/action_close").click()

    selected = whether_element_displayed(appium_driver, "id", "com.xueqiu.android:id/tab_name", wait_time=2)
    if not selected:
        appium_driver.tap([(size['width']/2, size['height']/2)])

    # 验证自选模块包含「阿里巴巴」
    appium_driver.find_element_by_xpath(".//android.widget.TextView[@text='自选']/..").click()
    appium_driver.find_element_by_xpath(".//android.widget.TextView[@text='阿里巴巴']")


if __name__ == '__main__':
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "demo",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
    test_xueqiu(driver)
    driver.quit()
