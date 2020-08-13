from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    added_date = models.DateTimeField(auto_now_add= False,auto_now = True)
    name = models.CharField(max_length = 50)
    description =models.TextField(max_length= 255,default = None)
    quantity = models.IntegerField()
    totalsale = models.IntegerField()
    capital_price = models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2,default=None)
    totalprofit = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

   
