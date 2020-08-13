from django.db import models
from Product.models import Product




# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.IntegerField(default = None)
    date = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=50,unique = True)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
    description = models.TextField(max_length = 255,default = None)
    # description = models.ForeignKey(
    #     Product,
    #     related_name = '+',
    #     on_delete = models.CASCADE,
    #     default = None,
        
    # )
    # amount = models.ForeignKey(
    #     Product,
    #     related_name = '+',
    #     on_delete = models.CASCADE,
    #     default = None,

    # )

    def __str__(self):
        return self.name
