from django.test import SimpleTestCase
from django.urls import reverse, resolve
from inventory.views import index, display_laptops, add_laptop

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_laptops_url_is_resolved(self):
        url = reverse('display_laptops')
        print(resolve(url))
        self.assertEquals(resolve(url).func, display_laptops)

    def test_add_laptops_url_is_resolved(self):
        url = reverse('add_laptop')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_laptop)