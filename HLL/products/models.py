from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default='SOME INTEGER')
    image = models.URLField()
    cart = models.BooleanField()

class cartItem(models.Model):
    cart_quantity = models.IntegerField()
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    cartUser = models.CharField(max_length=200, default='SOME STRING')
    


