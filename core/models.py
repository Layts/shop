from django.db import models
from django.conf import global_settings


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


