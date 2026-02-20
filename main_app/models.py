from django.db import models

# Create your models here.
class Bake(models.Model): 
    name = models.CharField(max_length=100)
    bakery=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    rating=models.IntegerField(default=5)
    price=models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return self.name