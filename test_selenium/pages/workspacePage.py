import logging
from pages.basePage import BasePage

logging.basicConfig(level=logging.INFO)


class WorkspacePage(BasePage):
    headTitle_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/span'

    def __init__(self, driver, base_url):
        BasePage.__int__(self, driver, base_url)

    def get_headTitle(self):
        return self.get_text(self.headTitle_xpath)
