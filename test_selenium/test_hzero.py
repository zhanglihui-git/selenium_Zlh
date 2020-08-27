import logging
import unittest
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(20)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#material/image')

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://gateway-uat.erp.ciec.com/oauth/login')
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Admin@123")
        self.driver.find_element_by_xpath('//*[@id="loginFormAccount"]/div[2]/span/button').click()
        self.driver.implicitly_wait(30)
        text1 = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/span').text
        assert '我的工作台' == text1
        # assert "我的工作台" in self.driver.page_source
        sleep(10)
        # self.driver.find_element_by_partial_link_text("登录").click()

    # def test_search(self):password").send_keys("Admin@123")
    # def test_firefox(self):
    #     self.driver.Firefox().get("http://testing-studio.com/")

    # def test_search(self):
    #     self.driver.
    #     #     self.driver.find_element_by_name("username").send_keys("admin")
    #     #     self.driver.find_element_by_id("get("https://www.baidu.com/")
    #     self.driver.implicitly_wait(3)
    #     self.driver.find_element_by_name("wd").send_keys("3333")
    #     sleep(20)

    # def test_explicit_wait(self):
    #     self.driver.find_element_by_partial_link_text("社区").click()
    #     self.driver.find_element_by_partial_link_text("最新发布").click()
    #     # self.driver.find_element_by_xpath('//ul/li/a[contains(text(),"最新发布")]').click()
    #     sleep(20)
    #     logging.info(time())
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".topic .title a")))
    #     logging.info(time())
