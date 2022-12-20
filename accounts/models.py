from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class personaldetails(models.Model):
    first_name=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    number=PhoneNumberField()
    address=models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name)