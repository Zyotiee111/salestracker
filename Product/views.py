from django.shortcuts import render,redirect
from Product.forms import ProductForm
from Product.models import Product

# Create your views here.

def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("show_product")
            except:
                pass
    else:
        form = ProductForm()
    return render(request, "product/addproduct.html", {'form': form})

def show(request):
    products = Product.objects.all()
    return render(request,"product/showproduct.html", {'products': products})


def edit(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("show_product")
    return render(request,"product/editproduct.html",{'form': form})


def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('show_product')