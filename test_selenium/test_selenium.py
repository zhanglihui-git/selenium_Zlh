import logging
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
        #self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(3)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#material/image')

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://testing-studio.com/')

    # def test_firefox(self):
    #     self.driver.Firefox().get("http://testing-studio.com/")

    def test_search(self):
        # self.driver.get("https://www.baidu.com/")
        # self.driver.implicitly_wait(3)
        self.driver.find_element_by_name("wd").send_keys("3333")
        sleep(20)

    def test_0430(self):
        # self.driver.find_element(By.CSS_SELECTOR, '.title [title*="第一季度招聘"]').click()
        # # self.driver.find_element_by_link_text("第六届中国互联网测试开发大会").click()
        # self.driver.find_element(By.XPATH, "//p/a[contains(@href, '22591')]").click()
        # for w in self.driver.window_handles:
        #     logging.info(w)
        # logging.info(self.driver.title)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # logging.info(self.driver.title)
        # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]").click()
        # self.driver.find_element(By.XPATH, '//ul/li/a[contains(@href,"#1.1")]').click()
        sleep(20)
        # for w in self.driver.window_handles:
        #     logging.info(w)
        #     self.driver.switch_to.window(w)
        #     logging.info()

    def test_explicit_wait(self):
        self.driver.find_element_by_partial_link_text("社区").click()
        self.driver.find_element_by_partial_link_text("最新发布").click()
        # self.driver.find_element_by_xpath('//ul/li/a[contains(text(),"最新发布")]').click()
        sleep(20)
        logging.info(time())
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".topic .title a")))
        logging.info(time())

    # def test_login(self):
    #     self.driver.find_element_by_partial_link_text("登录").click()
    #     element = self.driver.find_element_by_xpath('//form/div/input[@name="user[login]"]')
    #     logging.info(element.is_displayed())
    #     logging.info(element.id)
    #     logging.info(element.tag_name)
    #     logging.info(element.text)
    #     logging.info(element.location)
    #     logging.info(element.size)
    #     logging.info(element.rect)
    #     logging.info(element.get_attribute("placeholder"))
    #     element.click()
    #     self.driver.find_element_by_xpath('//form/div/input[@name="user[password]"]').send_keys("Zlh282616")
    #     self.driver.find_element_by_xpath('//label/input[@name="user[remember_me]" and @type="checkbox"]').click()
    #     self.driver.find_element(By.XPATH, '//div/input[@name="commit"]').click()
    #     sleep(10)
    #
    # def test_upload_file(self):
    #     self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector").click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".js_upload_label").click()