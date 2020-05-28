from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = '__all__'


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = '__all__'
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = '__all__'
