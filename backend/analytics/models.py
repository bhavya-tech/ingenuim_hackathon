from faulthandler import is_enabled
from itertools import product
from django.db import models
from indian_cities.dj_city import cities
# Create your models here.

class Region(models.Model):
    city = models.CharField(choices=cities, null=False, max_length=20)

    def __str__(self):
        return self.city

class Category(models.Model):
    name = models.CharField(max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=100)

###############################################################################################

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    # TODO: Add a field "price%"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images') #thumbnail
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    price = models.IntegerField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    type = models.ForeignKey("ProductType", on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    compare = models.BooleanField(default=False)
    stock_keeping_unit = models.CharField(max_length=10)
    quantity = models.IntegerField()

###############################################################################################

class Order(models.Model):
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)