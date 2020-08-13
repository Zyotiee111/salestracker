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
    description = models.CharField(max_length = 255, default = None)
    quantity = models.IntegerField(default= None)
    status =  models.CharField(max_length = 20,choices= choice )
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    dueamount = models.DecimalField(max_digits=10,decimal_places=2)

