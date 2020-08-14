from django.shortcuts import render,redirect
from  sales.forms import SalesForm
from  sales.models import Sales
from django.http import HttpResponse


def add(request):
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("sale:show_sale")
            except:
                return HttpResponse(form.errors)
    else:
        form = SalesForm()
    return render(request, "Sales/addsale.html", {'form': form})

def show(request):
    saless = Sales.objects.all()
    return render(request,"Sales/showsale.html", {'saless': saless})


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


