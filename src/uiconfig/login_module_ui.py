# -*- coding: utf-8 -*-
"""
记录登录相关的ui
"""

main_page_login_id = 'com.xueqiu.android:id/user_profile_container'

profile_login_button_id = 'com.xueqiu.android:id/tv_login'

wechat_login_button_id = 'com.xueqiu.android:id/rl_login_by_wx'
phone_or_others_login_button_id = 'com.xueqiu.android:id/tv_login_by_phone_or_others'

wechat_login_account_xpath = '//android.widget.EditText[contains(@text, "请填写微信号/QQ号/邮箱")]'
wechat_login_passwd_xpath = '//android.widget.EditText[contains(@text, "请填写密码")]'
wechat_login_commit_xpath = '//android.widget.Button[contains(@text, "登录")]'

wechat_install_notify_xpath = '//*[@text="登录后应用将获得以下权限"]'
wechat_install_login_xpath = '//android.widget.Button[@resource-id="com.tencent.mm:id/cov"]'
wechat_unauth_notify_xpath = '//android.widget.TextView[@text="该微信账号尚未被注册，是否立即注册雪球?"]'

wechat_login_error_notify_xpath = '//android.widget.TextView[contains(@text, "帐号或密码错误，请重新填写。")]'

phone_input_phone_id = 'com.xueqiu.android:id/register_phone_number'
phone_input_code_id = 'com.xueqiu.android:id/register_code'
phone_input_code_xpath = "//*[@text='请输入四位验证码']"
phone_commit_button_id = 'com.xueqiu.android:id/button_next'
phone_register_code_id = 'com.xueqiu.android:id/register_code_text'
phone_reget_code_xpath = '//android.widget.TextView[contains(@text, "获取验证码")]'
phone_registering_code_xpath = "//*[contains(@text, '重新获取')]"
phone_register_notify_id = 'com.xueqiu.android:id/md_title'
phone_commit_notify_id = 'com.xueqiu.android:id/md_content'
phone_commit_close_id = 'com.xueqiu.android:id/md_buttonDefaultPositive'

phone_send_code_toast_xpath = '//android.widget.Toast[@text="验证码已发送" or @text="验证码发送次数超出限制, 请明天再试"]'

notify_cancel_id = 'com.xueqiu.android:id/md_buttonDefaultNegative'


phone_email_login_button_id = 'com.xueqiu.android:id/tv_login_with_account'
phone_email_input_account_id = 'com.xueqiu.android:id/login_account'
phone_email_input_passed_id = 'com.xueqiu.android:id/login_password'
phone_email_commit_button_id = 'com.xueqiu.android:id/button_next'
phone_email_error_notify_xpath = '//android.widget.TextView[@text="用户名或密码错误" or @text="请求太频繁，请稍后再试"]'