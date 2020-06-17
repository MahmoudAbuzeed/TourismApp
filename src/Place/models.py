from django.db import models

class Place(models.Model) :
    name = models.CharField(max_length=50)
    address = models.TextField(default=' ')
    dates = models.CharField(max_length= 100)
    fees = models.IntegerField()
    image = models.ImageField()
    created = models.DateTimeField()




    def __str__(self):
        return self.name