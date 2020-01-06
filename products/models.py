from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
