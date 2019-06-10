# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "demon"
caps["appPackage"] = "com.cootek.smartdialer"
caps["appActivity"] = ".v6.TPDStartupActivity"
caps["autoGrantPermissions"] = True
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
caps["automationName"] = "uiautomator2"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RelativeLayout[4]/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
el2.click()
el3 = driver.find_element_by_id("com.cootek.smartdialer:id/nz")


# driver.execute_script('mobile: doubleTap', {'element': el3})

from appium.webdriver.common.touch_action import TouchAction
action = TouchAction(driver)
action.tap(element=el3, count=2).perform()


driver.quit()
