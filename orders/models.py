from django.db import models

# Create your models here.

size = (
    ("Small", "Small"),
    ("Large", "Large")
)

class subs(models.Model):
    name = models.CharField(max_length= 64)
    size = models.CharField(max_length= 10)
    price = models.DecimalField(max_digits= 5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.price}"

class pasta(models.Model):
    name = models.CharField(max_length= 64)
    price = models.DecimalField(max_digits= 5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class salads(models.Model):
    name = models.CharField(max_length= 64)
    price = models.DecimalField(max_digits= 5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class dinplatter(models.Model):
    name = models.CharField(max_length= 64)
    size = models.CharField(max_length= 10)
    price = models.DecimalField(max_digits= 5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.price}"
    
class toppings(models.Model):
    name = models.CharField(max_length= 64)

    def __str__(self):
        return f"{self.name}"

class regularpizza(models.Model):
    name = models.CharField(max_length = 64)
    size = models.CharField(max_length= 64)
    price = models.DecimalField(max_digits =5, decimal_places=2)
    numoftopp = models.DecimalField(max_digits= 2, decimal_places=0)
    #toppings = models.ForeignKey(toppi1ngs, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.price} - Toppings - {self.numoftopp}"

class silicanpizza(models.Model):
    name = models.CharField(max_length = 64)
    size = models.CharField(max_length= 64)
    price = models.DecimalField(max_digits =5, decimal_places=2)
    numoftopp = models.DecimalField(max_digits= 2, decimal_places=0)
    #toppings = models.ForeignKey(toppings, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.price} - Toppings - {self.numoftopp}"


class cart(models.Model):
    #cartid = models.DecimalField(max_digits= 10, decimal_places= 2)
    user = models.CharField(max_length = 255)
    category = models.CharField(max_length = 64)
    ordername = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f"{self.user} - {self.category} - {self.ordername}"

class orders(models.Model):
    orderid = models.IntegerField()
    user = models.CharField( max_length=255)
    category = models.CharField(max_length = 64)
    ordername = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.ordername}"


