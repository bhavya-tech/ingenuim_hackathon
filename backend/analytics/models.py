from django.db import models
from indian_cities.dj_city import cities
# Create your models here.

class Region(models.Model):
    city = models.CharField(choices=cities, null=False, max_length=20)

    def __str__(self):
        return self.city

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

###############################################################################################

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price_percentage = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.name

class Inventory(models.Model):
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images') #thumbnail
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    selling_price = models.FloatField(default=0.0)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    type = models.ForeignKey("ProductType", on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    compare = models.BooleanField(default=False)
    stock_keeping_unit = models.CharField(max_length=10)
    quantity = models.IntegerField()
    system_name = models.CharField(max_length=1000, blank=True, null=True ,default=None)

    def __str__(self) -> str:
        return self.name

    def get_price_range(self):
        return str(
            str(self.selling_price - (self.selling_price * self.type.price_percentage / 100)) 
            + "-" 
            + str(self.selling_price + (self.selling_price * self.type.price_percentage / 100))
        )

    def save(self, *args, **kwargs):
        self.system_name = str(
            str(self.type) + "_"
            + str(self.brand) + "_"
            + str(self.get_price_range()) + "_"
            + str(self.stock_keeping_unit)
        )
                        

###############################################################################################
class InventoryProduct(models.Model):
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    replenishing_quantity = models.IntegerField()
    rate = models.FloatField()

class Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)