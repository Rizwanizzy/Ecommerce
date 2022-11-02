from django.db import models
from shop.models import *

# Create your models here.


class cartlist(models.Model):
    cart_id = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)


class items(models.Model):
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.products
