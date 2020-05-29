from selenium import webdriver
from inventory.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class Testing(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def login_screen_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)

        alert = self.browser.find_element_by_class_name('content-section')
        self.assertEquals(
            alert.find_element_by_xpath('/html/body/div/div/form/div/button').is_displayed(), True)