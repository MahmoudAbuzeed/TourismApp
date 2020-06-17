from django.db import models
from Item.models import Item


class ItemImages(models.Model) :
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image1 = models.ImageField()
    altr1 = models.CharField(max_length=100)
    image2 = models.ImageField()
    altr2 = models.CharField(max_length=100)
    image3 = models.ImageField()
    altr3 = models.CharField(max_length=100)
    image4 = models.ImageField()
    altr4 = models.CharField(max_length=100)
    image5 = models.ImageField()
    altr5 = models.CharField(max_length=100)
    created  = models.DateTimeField()




    def __str__(self):
        return self.item
