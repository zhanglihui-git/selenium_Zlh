# coding:utf-8
import unittest
from time import sleep

from selenium import webdriver

from pages.loginPage import LoginPage
from pages.workspacePage import WorkspacePage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_case_login(self):
        self.url = u'http://gateway-uat.erp.ciec.com/oauth/login'
        self.userName = 'admin'
        self.passWord = 'Admin@123'
        Login_Page = LoginPage(self.driver, self.url)
        workspace_page = WorkspacePage(self.driver, self.url)
        Login_Page.gotoHZeroPage(self.url)
        Login_Page.input_username(self.userName)
        Login_Page.input_password(self.passWord)
        Login_Page.click_login()
        text = workspace_page.get_headTitle()
        assert '我的工作台' == text
        assert "我的工作台" in self.driver.page_source
        sleep(10)

    def tearDown(self):
        self.driver.quit()
