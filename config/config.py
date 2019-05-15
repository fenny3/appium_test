# -*- coding: utf-8 -*-
"""
存储相关的配置
"""
import os
routes = os.path.abspath(__file__).split('/')
print(routes)
ROOT = '/'.join(routes[:routes.index('appiumtest') + 1])
REPORT = os.path.join(ROOT, 'report')


CAPS = {
        "platformName": "Android",
        "deviceName": "demo",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "autoGrantPermissions": True,
        "newCommandTimeout": 120,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "automationName": "uiautomator2",
}

REMOTE_URL = "http://localhost:4723/wd/hub"

IMPLICITLY_WAIT_TIME = 15