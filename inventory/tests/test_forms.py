from django.test import  SimpleTestCase
from inventory.forms import LaptopForm, DesktopForm, MobileForm


class TestForms(SimpleTestCase):

    def test_laptop_form_valid_data(self):
        form = LaptopForm(data={
            'brand':'Lenovo',
            'modelis' : 'y312',
            'kiekis' : 21,
            'kaina' : 900
            })

        self.assertTrue(form.is_valid())

    def test_laptop_form_invalid_data(self):
        form = LaptopForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


    def test_mobile_form_valid_data(self):
        form = MobileForm(data={
            'brand':'Lenovo',
            'modelis' : 'y312',
            'kiekis' : 21,
            'kaina' : 900
            })

        self.assertTrue(form.is_valid())

    def test_mobile_form_invalid_data(self):
        form = MobileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_desktop_form_valid_data(self):
        form = DesktopForm(data={
            'brand':'Lenovo',
            'modelis' : 'y312',
            'kiekis' : 21,
            'kaina' : 900
            })

        self.assertTrue(form.is_valid())

    def test_desktop_form_invalid_data(self):
        form = DesktopForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)