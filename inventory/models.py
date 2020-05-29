from django.db import models

# Create your models here.

class Device(models.Model):

    brand = models.CharField(max_length=50, blank=False)
    modelis = models.CharField(max_length=200, blank=False)
    kiekis = models.IntegerField()
    kaina = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return 'Brandas: {0} Modelis: {1} Kaina: {2}'.format(self.brand, self.modelis, self.kaina)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass
