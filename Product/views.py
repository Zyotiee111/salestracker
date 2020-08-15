from django.shortcuts import render,redirect
from Product.forms import ProductForm
from Product.models import Product
from django.db.models import F

# Create your views here.

def track(request):
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

def display(request):
    products = Product.objects.all()
    return render(request,"product/showproduct.html", {'products': products})


def update(request, id):
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


def result(request):
    results = Product.objects.annotate(
             diff=F(selling_price) - F(capital_price)
         )
    return render(request, "Product/showproduct.html", {'results': results})

def sale_num(request,id):
    instance = Product.objects.get(id = id)
    salen = instance.totalsale + 1
    instance.totalsale = salen
    instance.save()
    return redirect('show_product')