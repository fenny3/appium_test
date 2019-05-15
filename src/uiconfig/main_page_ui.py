# -*- coding: utf-8 -*-
"""
记录主界面的页面元素
"""

# 雪球tab页面元素

xueqiu_button_id = 'com.xueqiu.android:id/button_icon'
xueqiu_label_xpath = '//*[contains(@resource-id,"indicator")]//*[@text="{text}"]'
xueqiu_label_by_brother_xpath = '//*[contains(@resource-id,"indicator")]//*[@text="{text}"]/../following-sibling::android.widget.RelativeLayout/android.widget.TextView'


## 基金新闻栏目
xueqiu_jijin_topic_xpath = '//*[contains(@resource-id, "topic_author") and contains(@text, "{text}")]'