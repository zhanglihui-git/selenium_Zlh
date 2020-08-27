from time import sleep

from selenium import webdriver


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_search(self):
        self.driver.get("http://testing-studio.com/")
        assert "测试开发" in self.driver.page_source
