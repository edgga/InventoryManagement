from django.test import TestCase, Client
from django.urls import reverse
from inventory.urls import *
from inventory.views import *
from inventory.models import Laptops, Mobiles, Desktops
import json


'''class TestViews(TestCase):

    def test_add_laptop(self):
        client = Client()
        response = client.get(reverse('display_laptops'))
        self.assertTemplateUsed(response, 'laptops/')
        self.assertEquals(response.status_code, 200)
'''