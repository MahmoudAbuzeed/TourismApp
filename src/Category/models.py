from django.db import models


class Category(models.Model) :
    name = models.CharField(max_length=50)
    created  = models.DateTimeField()


    def __str__(self):
        return self.name
