from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Bake(models.Model): 
    name = models.CharField(max_length=100)
    bakery = models.CharField(max_length=20, default="")
    description = models.TextField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bake-detail', kwargs={'pk': self.id})

RATINGS = (
    (1, '*'), 
    (2, '**'), 
    (3, '***'), 
    (4, '****'), 
    (5, '*****')
)
class Review(models.Model):
    rating = models.IntegerField(
        choices = RATINGS, 
        default = RATINGS[0][0]
    )
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    
    bake = models.ForeignKey(Bake, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']