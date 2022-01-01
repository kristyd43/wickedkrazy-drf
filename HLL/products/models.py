from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.URLField()
    cart = models.IntegerField()

class cartItem(models.Model):
    cart_quantity = models.IntegerField()
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    cartUser = models.CharField(max_length=200, default='SOME STRING')
    


