# coding:utf-8
from abc import ABC

import basepage as basepage
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.basePage import BasePage


class LoginPage(BasePage):
    search_by_name = "username"
    search_by_id = "password"
    login_path = "//*[@id='loginFormAccount']/div[2]/span/button"

    def __init__(self, driver, base_url):
        BasePage.__int__(self, driver, base_url)

    def gotoHZeroPage(self, base_url):
        print(u'打开HZero首页：', base_url)
        self.driver.get(base_url)

    def input_username(self, text=u'admin'):
        print(u'输入用户名：', text)
        self.input_text_byName(self.search_by_name, text)

    def input_password(self, text=u'Admin@123'):
        print(u'输入密码：', text)
        self.input_text_byId(self.search_by_id, text)

    # click 登录
    def click_login(self):
        self.click(self.login_path)
