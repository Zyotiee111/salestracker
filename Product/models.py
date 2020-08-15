from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    added_date = models.DateField()
    name = models.CharField(max_length = 50)
    description =models.TextField(max_length= 255,default = None)
    quantity = models.IntegerField()
    totalsale = models.IntegerField(editable = False, null = True)
    capital_price = models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    item_remaining = models.IntegerField(editable= False, null = True)
    totalprofit = models.DecimalField(max_digits=10,decimal_places=2,editable = False, null =True)

    def __str__(self):
        return self.name

   
