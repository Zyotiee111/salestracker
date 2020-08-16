from django.shortcuts import render,redirect
from  sales.forms import SalesForm, InvoiceeForm
from  sales.models import Sales, Invoice
from sales.forms import InvoiceeForm
from Product.models import Product
from customer.models import Customer
from django.http import HttpResponse
from django.db.models import Q

import datetime


def add(request):
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            status = form.cleaned_data['status']
            sold_to = form.cleaned_data['sold_to']
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            product = Product.objects.get(name=item)
            product_id = product.id
            capital_price = product.capital_price
            selling_price = product.selling_price
            discount = product.discount
            total = quantity * (selling_price - discount)
            customer = Customer.objects.get(name= sold_to)
            sold_to = customer.id

            product = Product.objects.get(id=product_id)
            if product.item_remaining is None:
                product.item_remaining = product.quantity
            print(product.item_remaining)
            product.item_remaining = product.item_remaining - quantity
            if product.totalsale is None:
                product.totalsale = 0
            product.totalsale += quantity
            print(product.totalsale)

            # product.quantity = product.quantity- quantity
            # product.totalsale += quantity
            # if product.item_remaining is None:
            #     product.item_remaining = 0
            # product.item_remaining = product.totalsale + product.quantity
           
            if product.totalprofit is None:
                product.totalprofit = 0
            product.totalprofit = product.totalprofit +(( selling_price- discount)- capital_price ) * quantity 
            product.save() 
            
            Sales.objects.create(
                date = date,
                sold_to = customer,
                item = product,
                quantity = quantity,
                amount= selling_price,
                status = status,
                dueamount = 0,
                Discount = product.discount,
                Total = total
            )
            return redirect("sale:show_sale")
    else:
        form = SalesForm()
    return render(request, "Sales/addsale.html", {'form': form})

def show(request):
    saless = Sales.objects.all()
    return render(request,"Sales/showsale.html",{'saless':saless})


def edit(request, id):
    sales = Sales.objects.get(id=id)
    form = SalesForm(request.POST or None, instance=  sales)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("sale:show_sale")
    return render(request,"Sales/editsale.html",{'form': form})


def delete(request,id):
    sales = Sales.objects.get(id=id)
    sales.delete()
    return redirect("sale:show_sale")

def create(request):
    if request.method == "POST":
        form =InvoiceeForm(request.POST)
        if form.is_valid():
          sold_to =  form.cleaned_data['sold_to']
          customer = Customer.objects.get(name=sold_to)
          sales_trans = Sales.objects.filter(sold_to=customer)
          for sale in sales_trans:
              s = Sales.objects.get(sold_to=customer, item=sale.item)
              if  s.count() > 0:
                  dueamount += s.dueamount
                  quantity += s.quantity
                  discount += s.Discount
                  total += s.Total
          Invoice.objects.create(
              date = datetime.date.today(),
              sold_to = s.sold_to,
              item = s.item,
              quantity = quantity,
              amount= s.amount,
              status = s.status,
              dueamount = 0,
              Discount = discount,
              Total = total

          )
        

        #   total_sum = 0
        #   for s_item in sales_trans:
        #       total_sum += s_item.Total
        #   context  = {
        #       'sales': sales_trans,
        #       'total_sum': total_sum,
        #    }
          return render(request, "Invoice/test.html", context)
    else:
        form = InvoiceeForm()
    return render(request, "Invoice/createinvoice.html", {'form': form})







