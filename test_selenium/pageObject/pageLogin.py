import logging
from time import sleep, time
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


class PageLogin(object):

    # username
    loginUsn = 'admin'
    # password
    loginPwd = 'Admin@123'
    # HZero Url
    baseUrl = 'http://gateway-uat.erp.ciec.com/oauth/login'

    def input_username(self):
        self.driver.find_element_by_name("username").send_keys("admin")

    def input_password(self):
        self.driver.find_element_by_id("password").send_keys("Admin@123")
    self.driver.get('http://gateway-uat.erp.ciec.com/oauth/login')
    self.driver.find_element_by_xpath('//*[@id="loginFormAccount"]/div[2]/span/button').click()
    self.driver.implicitly_wait(30)
    text1 = self.driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/span').text
