from django.db import models
from customer.models import Customer
from Product.models import Product

choice = (
    ('paid','paid'),
    ('due','due'),
)

# Create your models here.
class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    sold_to = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name ="+") 
    item = models.ForeignKey(Product, on_delete = models.CASCADE, related_name ="+")
    quantity = models.IntegerField(default= None)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status =  models.CharField(max_length = 20,choices= choice )
    dueamount = models.DecimalField(max_digits=10,decimal_places=2)
    Discount = models.DecimalField(max_digits=10,decimal_places=2,default = None)
    Total = models.DecimalField(max_digits=10,decimal_places=2,default = None)

