from django.db import models
from customer.models import Customer
from Product.models import Product

choice = (
    ('paid','paid'),
    ('due','due'),
)

# Create your models here.
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    invoice_for = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name ="+") 
    item = models.ForeignKey(Product, on_delete = models.CASCADE, related_name ="+")
    description = models.CharField(max_length = 255, default = None)
    quantity = models.IntegerField(default= None)
    status =  models.CharField(max_length = 20,choices= choice )
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    dueamount = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2, default = None)

