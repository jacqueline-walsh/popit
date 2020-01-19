from datetime import datetime
from django.db import models
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    stock = models.IntegerField()

    def __str__(self):
        return self.name

