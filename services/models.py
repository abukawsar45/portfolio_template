from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    cover = models.ImageField()

    def __str__(self):
        return self.name
