from shop.models import product
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class cartlist(models.Model):
    cart_id = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)


class items(models.Model):
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.products

    def total(self):
        return self.products.price*self.quantity


class del_details(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    number=models.IntegerField()
    landmark=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    address_type=models.CharField(max_length=255)

    def __str__(self):
        return self.username

class orders(models.Model):
    product=models.CharField(max_length=255)
    price=models.IntegerField()
    delivery_date=models.DateField()

    def __str__(self):
        return self.name




