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
caps["chromedriverExecutableDir"] = "/Users/feeny/Documents/chromedriver/"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)


el1 = driver.find_element_by_xpath("//*[@text='找优惠']")
el1.click()
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[4]/android.view.View")
# el2.click()
# el3 = driver.find_element_by_xpath("//*[@text='请输入手机号']")
# el3.send_keys("13800000000")
# el4 = driver.find_element_by_xpath("//*[@text='发送验证码']")
# el4.click()


### 没有开启webview debug的app，是不能够切换为webview进行测试的。
action = TouchAction(driver)
action.tap(element=None, x=100, y=600, count=2).perform()


driver.execute_script()

print(driver.contexts)
print(driver.current_context)
driver.switch_to.context(driver.contexts[-1])
print(driver.current_context)
print(driver.current_window_handle)
print(driver.window_handles)
print(driver.current_window_handle)
print(driver.title)
# driver.switch_to.window(driver.window_handles[-1]) 不能这样随意切换，需要看看是不是需要切换，可以根据获取到的title做对比决定
print(driver.title)
driver.find_element_by_css_selector('.dp_my_home').click()
print(driver.current_window_handle)
print(driver.window_handles)
driver.find_element_by_css_selector('input[name="mobile"]').send_keys('13800000000')
driver.find_element_by_css_selector('.J_send.EasyLogin_send').click()

driver.quit()
