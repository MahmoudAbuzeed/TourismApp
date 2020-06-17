from django.db import models
from Place.models import Place


class PlaceImages(models.Model) :
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image1 = models.ImageField()
    altr1 = models.CharField(max_length=100)
    image2 = models.ImageField()
    altr2 = models.CharField(max_length=100)
    image3 = models.ImageField()
    altr3 = models.CharField(max_length=100)
    created = models.DateTimeField()




    def __str__(self):
        return self.place