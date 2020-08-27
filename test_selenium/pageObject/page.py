import logging
from time import sleep, time
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


class Page(object):
    """Page 基类，所有page都应继承该类"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


