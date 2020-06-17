from django.db import models
from Place.models import Place

class Item(models.Model) :
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default= ' ')
    voiceNote = models.FileField(max_length=150)
    qrImage = models.ImageField()
    noOfScans = models.IntegerField()
    created  = models.DateTimeField()


    def __str__(self):
        return self.name

