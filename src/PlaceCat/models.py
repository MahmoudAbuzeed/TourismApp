from django.db import models
from Place.models import Place
from Category.models import Category

class PlaceCat(models.Model) :
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rank = models.IntegerField()
    created = models.DateTimeField()





    def __str__(self): 
        return self.place
