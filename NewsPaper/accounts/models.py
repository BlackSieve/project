from django.db import models


class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    labor_contact = models.IntegerField


class ProductOrder(models.Model):
    pass