from django.test import TestCase
from django.urls import reverse, resolve
from inventory.views import index, display_laptops, add_laptop
from selenium import webdriver
from inventory.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class TestModels(TestCase):

    def setUp(self):
        self.device1 = Laptops.objects.create(
            brand = 'HP',
            modelis = '22x',
            kaina = 1000,
            kiekis = 100
        )

    def test_laptop_is_created(self):
        self.assertEquals(self.device1.kaina, 1000)

    def test_mobile_is_created(self):
        self.assertEquals(self.device1.kiekis, 100)

    def test_mobile_is_created(self):
        self.assertEquals(self.device1.brand, 'HP')


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