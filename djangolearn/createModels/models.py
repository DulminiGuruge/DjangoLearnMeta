from django.db import models

# Create your models here.
#Week 3 - Creating models

class Menu(models.Model):
    name= models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()
    #now add the Menu to settings

    def __str__(self):
        return self.name + " : " + self.cuisine



