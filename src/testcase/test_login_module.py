# -*- coding: utf-8 -*-
"""
完成雪球登录场景的测试
要去带有setup_class setup_method体系
微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
"""

import sys
sys.path.append('/Users/feeny/Touchpal/appiumtest')
import logging

import pytest
import allure
from appium.webdriver.webdriver import WebDriver

from src.common.driver import AppDriver
from config import config as Config

from src.uiconfig import login_module_ui as LoginUI


logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s %(asctime)s %(filename)s %(funcName)s line:%(lineno)d]: %(message)s',
                    datefmt='%y%m%d %H:%M:%S')

@allure.feature('测试登录模块')
class TestLogin:
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        cls.app_driver = AppDriver(Config.REMOTE_URL, Config.CAPS, Config.IMPLICITLY_WAIT_TIME)
        cls.driver = cls.app_driver.driver
        cls.win_size = cls.app_driver.window_size

    def setup_method(self):
        """
        每个case执行前进入登录页面
        :return: 
        """
        self.driver.find_element_by_id(LoginUI.main_page_login_id).click()
        self.driver.find_element_by_id(LoginUI.profile_login_button_id).click()

    @allure.story('测试微信登录——未安装微信')
    @allure.title('测试不合法的帐号密码无法登录并给出提示')
    @pytest.mark.parametrize('account, passwd', [('13800000000', '1234')])
    def test_wechat_1(self, account, passwd):
        """
        输入不合法的帐号，密码，测试错误提示
        """
        with allure.step('点击微信登录按钮，进入微信登录页面'):
            self.driver.find_element_by_id(LoginUI.wechat_login_button_id).click()
        with allure.step('输出帐号，验证码，点击登录按钮'):
            if self.app_driver.whether_element_displayed('xpath', LoginUI.wechat_install_notify_xpath, wait=10) or \
                    self.app_driver.whether_element_displayed('xpath', LoginUI.wechat_unauth_notify_xpath, wait=10):
                logging.info('已安装微信，跳过此case')
                pytest.skip("已安装微信，跳过此case")
            else:
                self.driver.find_element_by_xpath(LoginUI.wechat_login_account_xpath).send_keys(account)
                self.driver.find_element_by_xpath(LoginUI.wechat_login_passwd_xpath).send_keys(passwd)
                self.driver.find_element_by_xpath(LoginUI.wechat_login_commit_xpath).click()
                with allure.step('不合法的帐号、密码，提示登录错误'):
                    self.driver.find_element_by_xpath(LoginUI.wechat_login_error_notify_xpath)

    @allure.story('测试微信登录——已安装微信')
    @allure.title('测试点击微信登录跳转授权的功能')
    def test_wechat_2(self,):
        """
        输入不合法的帐号，密码，测试错误提示
        """
        with allure.step('点击微信登录按钮，进入微信登录页面'):
            self.driver.find_element_by_id(LoginUI.wechat_login_button_id).click()
        with allure.step('输出帐号，验证码，点击登录按钮'):
            first_notify = self.app_driver.whether_element_displayed('xpath', LoginUI.wechat_install_notify_xpath, wait=10)
            auth_notify = self.app_driver.whether_element_displayed('xpath', LoginUI.wechat_unauth_notify_xpath, wait=10)
            if first_notify or auth_notify:
                if first_notify:
                    self.driver.find_element_by_xpath(LoginUI.wechat_install_login_xpath).click()
                self.driver.find_element_by_xpath((LoginUI.wechat_unauth_notify_xpath))
                self.driver.find_element_by_id(LoginUI.notify_cancel_id).click()
            else:
                logging.info('未安装微信，跳过此case')
                pytest.skip("未安装微信，跳过此case")

    @allure.story('测试手机及其他登录')
    @allure.title('测试手机号及验证码登录方式')
    @pytest.mark.parametrize('phone, code', [('13800000002','1234'),
                                             ('13800000003','12'),
                                             ('13800000004','12345'),
                                             ('8613800000000', '1234'),
                                             ('1380000000', '1234'),])
    def test_2(self, phone, code):
        with allure.step('点击手机及其他登录按钮，进入手机登录页面'):
            self.driver.find_element_by_id(LoginUI.phone_or_others_login_button_id).click()
        with allure.step('验证发送验证码按钮是否可点击,可点击时取获取验证码'):
            self.driver.find_element_by_id(LoginUI.phone_input_phone_id).send_keys(phone)
            register_code_button = self.driver.find_element_by_id(LoginUI.phone_register_code_id)
            logging.info(register_code_button.get_attribute('clickable'))
            if len(phone) != 11:
                assert register_code_button.get_attribute('clickable') == 'false'
            else:
                assert register_code_button.get_attribute('clickable') == 'true'
                with allure.step('验证正在获取验证码'):
                    register_code_button.click()
                    self.driver.find_element_by_xpath(LoginUI.phone_send_code_toast_xpath)
                    logging.info('有toast提示')
                    if self.app_driver.whether_element_displayed('xpath', LoginUI.phone_registering_code_xpath, wait=2):
                        logging.info('验证码已发送')
                        with allure.step('关闭语音验证的提示'):
                            self.app_driver.wait_element_displayed('id', LoginUI.phone_register_notify_id, wait=50)
                            logging.info('显示语音提示框')
                            self.driver.find_element_by_id(LoginUI.notify_cancel_id).click()
                            logging.info('获取验证码结束')
                    else:
                        self.driver.find_element_by_xpath(LoginUI.phone_reget_code_xpath)
                        logging.info('获取验证码已经到达次数')
                with allure.step('验证输入不同的验证码，登录按钮是否可点击'):
                    try:
                        self.driver.find_element_by_id(LoginUI.phone_input_code_id).send_keys(code)
                    except:
                        print(self.driver.page_source)
                    commit_button = self.driver.find_element_by_id(LoginUI.phone_commit_button_id)
                    logging.info(commit_button.get_attribute('clickable'))
                    if len(code) != 4:
                        assert commit_button.get_attribute('clickable') == 'false'
                    else:
                        assert commit_button.get_attribute('clickable') == 'true'
                        commit_button.click()
                        self.driver.find_element_by_id(LoginUI.phone_commit_notify_id)
                        self.driver.find_element_by_id(LoginUI.phone_commit_close_id).click()

    @allure.story('测试手机及其他登录')
    @allure.title('测试邮箱手机号密码登录,错误的帐号登录')
    @pytest.mark.parametrize('account, passwd', [('13800000000', '123456'),('13800000000@163.com', '123456')])
    def test_3(self, account, passwd):
        with allure.step('点击手机及其他登录按钮，进入手机登录页面'):
            self.driver.find_element_by_id(LoginUI.phone_or_others_login_button_id).click()
        with allure.step('点击邮箱手机号密码登录'):
            self.driver.find_element_by_id(LoginUI.phone_email_login_button_id).click()
        with allure.step('输出邮箱或手机号'):
            self.driver.find_element_by_id(LoginUI.phone_email_input_account_id).send_keys(account)
            self.driver.find_element_by_id(LoginUI.phone_email_input_passed_id).send_keys(passwd)
        with allure.step('输入错误的手机号及密码，提示错误'):
            self.driver.find_element_by_id(LoginUI.phone_email_commit_button_id).click()
            self.driver.find_element_by_xpath(LoginUI.phone_email_error_notify_xpath)

    @allure.story('测试手机及其他登录')
    @allure.title('测试第三方登录')
    @pytest.mark.parametrize('third', ['com.xueqiu.android:id/sina_login',
                                       'com.xueqiu.android:id/tencent_login',
                                       'com.xueqiu.android:id/weixin_login',])
    def test_4(self, third):
        with allure.step('点击手机及其他登录按钮，进入手机登录页面'):
            self.driver.find_element_by_id(LoginUI.phone_or_others_login_button_id).click()
        with allure.step('点击第三方icon，开始登录'):
            logging.info('第三方icon的id为：{}'.format(third))
            self.driver.find_element_by_id(third).click()
            if not self.app_driver.whether_element_displayed('xpath', LoginUI.phone_email_login_button_id, wait=5):
                self.driver.back()

    def teardown_method(self):
        self.app_driver.restart_app()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__=='__main__':
    import os
    import subprocess

    xml_report_path = os.path.join(Config.REPORT, 'xml')
    logging.info(xml_report_path)
    html_report_path = os.path.join(Config.REPORT, 'html')
    pytest.main(['-s', '-v', '--alluredir', xml_report_path, 'src/testcase/test_login_module.py'])
    cmd = 'allure generate --clean {xml} -o {html}'.format(xml=xml_report_path, html=html_report_path)
    logging.info(cmd)
    subprocess.call(cmd, shell=True)


