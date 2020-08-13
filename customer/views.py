from django.shortcuts import render
from django.shortcuts import render,redirect
from customer.forms import CustomerForm
from customer.models import Customer
from django.http import HttpResponse


# Create your views here.



def add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("customer:show_customer")
            except:
                return HttpResponse(form.errors)
    else:
        form = CustomerForm()
    return render(request, "Customer/addcustomer.html", {'form': form})

def show(request):
    customers = Customer.objects.all()
    return render(request,"Customer/showcustomer.html", {'customers': customers})


def edit(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance= customer)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("customer:show_customer")
    return render(request,"Customer/editcustomer.html",{'form': form})


def delete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("customer:show_customer")
