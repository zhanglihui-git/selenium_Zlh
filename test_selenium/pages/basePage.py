# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

'''
公共方法封装:
1.打开浏览器
2.找元素
3.switch_to
4.send_keys
'''


class BasePage(object):
    """Page基类，所有page都应该继承该类"""

    def __int__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        # self.timeout = 30

    def input_text_byName(self, loc, text):
        self.driver.find_element_by_name(loc).send_keys(text)

    def input_text_byId(self, loc, text):
        self.driver.find_element_by_id(loc).send_keys(text)

    def click(self, loc):
        self.driver.find_element_by_xpath(loc).click()

    def get_text(self, loc):
        return self.driver.find_element_by_xpath(loc).text
